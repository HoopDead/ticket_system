""" Imports for: Sign up From """
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SignUpForm(UserCreationForm):
    
    username = forms.CharField(max_length = 32, required = True, widget = forms.TextInput(attrs = {'class': 'form-control'}))
    email = forms.CharField(max_length = 100, required = False, widget = forms.TextInput(attrs = {'class': 'form-control'}))
    password = forms.CharField(max_length = 256, required = True, widget = forms.PasswordInput(attrs = {'class': 'form-control'}))
    password_repeat = forms.CharField(max_length = 256, required = True, widget = forms.PasswordInput(attrs = {'class': 'form-control'}))

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'password_repeat']