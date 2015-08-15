__author__ = 'derek'

from django import forms

class UploadImageForm(forms.Form):
    image = forms.ImageField()


