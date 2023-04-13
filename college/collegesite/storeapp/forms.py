from django import forms
from .models import *
from django.forms import fields

class ApplicationForm(forms.ModelForm):
    date_of_birth = fields.DateField(widget=forms.widgets.DateInput(attrs={'type': 'date'}))
    class Meta:
        model = Application
        fields = ('name', 'date_of_birth', 'age', 'gender', 'address','phone_number','email', 'department', 'course','purpose')
