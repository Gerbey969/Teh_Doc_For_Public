from django.shortcuts import render
from django.http import HttpResponse
from django.core.mail import send_mail, BadHeaderError
from .models import *
from teh_doc.settings import *
from .forms import *
import smtplib
from django.views.generic import DetailView, ListView
from django.http import HttpResponse
from django.shortcuts import render
from django.core.mail import EmailMessage
from email.mime.text import MIMEText
from email.header import Header
from django.core.mail import EmailMultiAlternatives
from django.contrib.auth import authenticate, login
from django.template import loader
from django.shortcuts import redirect
from datetime import date


def feedback(request):
    form = FeedbackForm(request.POST, request.FILES or None)
    # model = form.model.objects.filter(feedback__category__name__contains=form.category)

    if request.method == 'POST':
        if form.is_valid():
            cd = form.cleaned_data
            data = request.POST
            name = data.get('name')
            email = data.get('email')
            phone = data.get('phone')
            category = data.get('category')
            country = data.get('country')
            ser_num = data.get('ser_num')
            description = data.get('description')
            today = date.today()
            order = Feedback.objects.create(name=cd['name'], email=cd['email'], phone=cd['phone'],
                                            category=cd['category'], ser_num=cd['ser_num'], country=cd['country'],
                                            description=cd['description'], date=today)

            smtp = smtplib.SMTP('smtp.gmail.com', 587)
            smtp.starttls()
            smtp.login(EMAIL_HOST_USER, EMAIL_HOST_PASSWORD)

            category_name = Category.objects.get(id=category)
            country_name = Documentation.objects.get(id=country)

            subject = Header('Prana Teh-Doc', 'utf-8')
            body = '<div style="margin: auto;border-radius:30px;border:0;">' \
                   + '<h2 style="color:black;text-align:center;"><strong>Нове Звернення</strong></h2>' \
                   + '<h3 style="color:black;text-align:left;">Дата: ' + str(today) + '</h3>'\
                   + "<h3 style='color:black;text-align:left;'>Ім'я: " + name + "</h3>" \
                   + "<h3 style='color:black;text-align:left;'>Email: " + email + "</h3>" \
                   + "<h3 style='color:black;text-align:left;'>Номер телефону: " + str(phone) + "</h3>" \
                   + "<h3 style='color:black;text-align:left;'>Країна: " + country_name.name + "</h3>" \
                   + "<h3 style='color:black;text-align:left;'>Категорія: " + category_name.name + "</h3>" \
                   + "<h3 style='color:black;text-align:left;'>Серійний номер: " + str(ser_num) + "</h3>" \
                   + "<h3 style='color:black;text-align:left;'>Опис: " + str(description) + "</h3>" + "</div>"

            from_email = EMAIL_HOST_USER

            msg = EmailMultiAlternatives(subject, body, from_email, [from_email])
            msg.attach_alternative(body, "text/html")
            if request.FILES:
                uploaded_file = request.FILES['file']
                msg.attach(uploaded_file.name, uploaded_file.read(), uploaded_file.content_type)
            msg.send()
    else:
        form = FeedbackForm()

    return render(request, 'feedback/feedback.html', {'form': form})
