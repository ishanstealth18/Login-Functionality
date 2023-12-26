from django import forms

from email_confirmation.models import Register_Table
from django.forms import ModelForm


class SignupForm(forms.ModelForm):
    class Meta:
        model = Register_Table
        fields = ['firstname', 'lastname', 'email', 'phone']


