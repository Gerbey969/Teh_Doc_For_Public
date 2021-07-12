from django.forms import *
from django import forms
from .models import *
from django.utils.translation import ugettext_lazy


class LoginForm(forms.Form):
    username = forms.CharField(label='Username', required=True, widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Username',
    }))
    password = forms.CharField(label='Password', required=True, widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'placeholder': 'Password',
    }))


class QRForm(forms.Form):
    name = forms.CharField(label='Name', required=True, widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Name',
    }))
    url = forms.URLField(label='URL', required=True, widget=forms.URLInput(attrs={
        'class': 'form-control',
        'placeholder': 'URL',
    }))
