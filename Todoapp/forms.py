from django import forms
from .models import *
from django.forms import ModelForm

class LoginForm(ModelForm):
    class Meta:
        model=Form
        fields='__all__'