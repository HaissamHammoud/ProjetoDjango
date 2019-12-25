from django import forms
from django.forms import ModelForm
from .models import Car

class CarForms(ModelForm):
    class Meta:
        model = Car
        fields = [
        'modelo',
        'placa',

        ]
