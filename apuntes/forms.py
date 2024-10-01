from django.forms import ModelForm

from .models import apuntes, Asignaturas
from django import forms
import django
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.db.models import fields
from django.http import request

class cons_apunt(forms.Form):
    nombre_tema = forms.CharField(label='nombre del tema', max_length=1000)



