from django import forms
from .models import *


class CustomForm(forms.Form):
    name = forms.CharField()
    addr = forms.CharField()









