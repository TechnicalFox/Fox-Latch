from django import forms
from django.contrib.auth.models import User
from django.forms import ModelForm
from fox.models import Fox

class RegistrationForm(ModelForm):
    