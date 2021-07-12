from django.shortcuts import render
from django.http import HttpResponse
from django.core.mail import send_mail, BadHeaderError
from .models import *
from .forms import *
from django.views.generic import DetailView, ListView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.defaults import page_not_found
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from .forms import LoginForm
from django.template import loader
from django.shortcuts import redirect


def handler404(request, exception):
    return render(request, 'landing/home.html', locals())


def handler500(request):
    return render(request, 'landing/home.html', locals())


def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            t = loader.get_template('landing/zavod.html')
            cd = form.cleaned_data
            user = authenticate(username=cd['username'], password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect("/zavod/")
                else:
                    return HttpResponse('Disabled account')
            else:
                return HttpResponse('Invalid login')
    else:
        form = LoginForm()
    return render(request, 'landing/login.html', {'form': form})


def home(request):
    country = Documentation.objects.filter(is_active=True)

    return render(request, 'landing/home.html', locals())


def country(request, country_id):
    countries = Documentation.objects.get(id=country_id)
    prana = Recuperator.objects.filter(is_active=True, country=country_id, not_for_zavod=False)
    prana__not__zavod = Recuperator.objects.filter(is_active=True, country=country_id, not_for_zavod=True).order_by(
        '-created')

    session_key = request.session.session_key
    if not session_key:
        request.session.cycle_key()

    print(request.session.session_key)

    return render(request, 'landing/country.html', locals())


def models(request, country_id, prana_id):
    country = Documentation.objects.get(id=country_id, is_active=True)
    prana = Recuperator.objects.get(id=prana_id, is_active=True)
    titles = Titles.objects.filter(is_active=True, country__id=country_id)
    revision = Revision.objects.filter(recuperator_id=prana_id, is_active=True)
    if revision:
        date = Revision.objects.filter(recuperator_id=prana_id, is_active=True).latest("date")
    garantiya = Garantiya.objects.filter(country__id=country_id)
    document = DocumentFiles.objects.filter(revision__recuperator_id=prana_id, is_active=True)
    dodatkove = Dodatkove.objects.filter(model__id=prana_id, is_active=True)

    session_key = request.session.session_key
    if not session_key:
        request.session.cycle_key()

    print(request.session.session_key)

    return render(request, 'landing/prana.html', locals())


def download(request):
    app = Download.objects.filter(is_active=True)

    return render(request, 'landing/download.html', locals())


def revisions(request, country_id, prana_id, revision_id):
    country = Documentation.objects.get(id=country_id, is_active=True)
    prana = Recuperator.objects.get(id=prana_id, is_active=True)
    revision = Revision.objects.get(id=revision_id, is_active=True)

    for_zav = DocumentFiles.objects.filter(revision__id=revision_id, is_active=True, for_zavod=True,
                                           for_manager=False, for_people=False)
    for_man = DocumentFiles.objects.filter(revision__id=revision_id, is_active=True, for_zavod=False,
                                           for_manager=True, for_people=False)
    document = DocumentFiles.objects.filter(revision__id=revision_id, is_active=True, for_zavod=True,
                                            for_manager=True, for_people=True)
    for_seperate = DocumentFiles.objects.filter(revision__id=revision_id, is_active=True, for_zavod=False,
                                                for_manager=True, for_people=True)
    for_sep = DocumentFiles.objects.filter(revision__id=revision_id, is_active=True, for_zavod=True,
                                           for_manager=True, for_people=False)
    for_s = DocumentFiles.objects.filter(revision__id=revision_id, is_active=True, for_zavod=False,
                                         for_manager=True, for_people=True)
    all_doc = DocumentFiles.objects.filter(revision__id=revision_id, is_active=True, for_zavod=True,
                                           for_manager=True, for_people=True)

    youtube = YouTube.objects.filter(model__id=revision_id, is_active=True)

    return render(request, 'landing/revision.html', locals())


def countriess(request):
    country = Documentation.objects.filter(is_active=True)

    return render(request, 'landing/countries.html', locals())


@login_required(login_url="/accounts/login/")
def qr(request):
    qr_codes = QRCodeGenerator.objects.filter(is_active=True)

    if request.method == 'POST':
        form = QRForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            data = request.POST
            name = data.get("name")
            url = data.get("url")

            order = QRCodeGenerator.objects.create(name=cd['name'], url=cd['url'])
    else:
        form = QRForm()

    return render(request, 'landing/qr_codes.html', locals())


@login_required(login_url="/accounts/login/")
def assortiment(request):
    country = Documentation.objects.filter(is_active=True)

    return render(request, 'landing/zavod.html', locals())


def extra_country(request, extra_id):
    extra = Documentation.objects.get(extra=extra_id)
    response = redirect('/country/' + str(extra.id) + "/")

    return response
