from django.forms import *
from django import forms
from .models import *
from landing.models import *
from django.utils.translation import ugettext_lazy


class FeedbackForm(forms.ModelForm):

    class Meta:
        model = Feedback
        exclude = [""]

    def __init__(self, *args, **kwargs):
        country = Documentation.objects.filter(is_active=True).values_list('id', 'name')
        category = Category.objects.filter(is_active=True).values_list('id', 'name')
        super(FeedbackForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget = TextInput(attrs={
            'class': 'form-control',
            'type': 'text',
            'name': 'author',
            'placeholder': ugettext_lazy('Name*'),
        })
        self.fields['email'].widget = EmailInput(attrs={
            'class': 'form-control',
            'type': 'email',
            'name': 'author',
            'placeholder': ugettext_lazy('Email*')
        })
        self.fields['phone'].widget = NumberInput(attrs={
            'class': 'form-control',
            'name': 'author',
            'placeholder': ugettext_lazy('Phone*')
        })
        self.fields['ser_num'].widget = NumberInput(attrs={
            'class': 'form-control',
            'name': 'author',
            'placeholder': ugettext_lazy('Serial Number')
        })
        self.fields['description'].widget = Textarea(attrs={
            'class': 'form-control',
            'name': 'author',
            'placeholder': ugettext_lazy('Description*')
        })
        self.fields['category'].widget = Select(choices=category, attrs={
            'class': 'form-control',
            'name': 'author',
            'placeholder': ugettext_lazy('Category*')
        })
        self.fields['country'].widget = Select(choices=country, attrs={
            'class': 'form-control',
            'name': 'author',
            'placeholder': ugettext_lazy('Country*')
        })
