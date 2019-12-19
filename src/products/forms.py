from django import forms
from django.forms import ModelForm
from .models import Product

class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = [
        'title',
        'description',
        'price'
        ]

class RawProductForm(forms.Form):
    title  = forms.CharField(widget = forms.Textarea(attrs={"placeholder": "title"}))
    description = forms.CharField(required = False, widget = forms.Textarea(
        attrs = {
            "class": "new-class-name two",
            "rows" : 10,
            "cols": 100
        }
        ))
    price   = forms.DecimalField()
