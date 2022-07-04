from dataclasses import field
from tkinter.tix import Form
from django import forms
from newapp.models import *

class formname(forms.ModelForm):
    class Meta:
        model = student
        fields = ('__all__')

class studentform(forms.ModelForm):
    class Meta:
        model = student
        fields = ('Name',)