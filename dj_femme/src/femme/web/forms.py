from django import forms
from django.forms import DateInput
from django.forms import EmailInput
from django.forms.widgets import TextInput
from django.utils.translation import gettext_lazy as _
from web.models import RegistrationClass


class RegistrationForm(forms.ModelForm):
    class Meta:
        model = RegistrationClass
        # fields = ['name', 'email']
        # exclude = ['email', 'phone']
        fields = '__all__'

        widgets = {
            'name': TextInput(attrs={'class': 'required', 'placeholder': 'Name'}),
            'email': EmailInput(attrs={'class': 'required', 'placeholder': 'Email'}),
            'phone': TextInput(attrs={'class': 'required', 'placeholder': 'Phone'}),
            'education': TextInput(attrs={'class': 'required', 'placeholder': 'Education'}),
            'dob': DateInput(attrs={'class': 'required', 'placeholder': 'Date of Birth'}),
            'message': TextInput(attrs={'class': 'required', 'placeholder': 'Message'}),
        }

        error_messages = {
            'name': {
                'required': _("Name field is required!"),
            },
            'email': {
                'required': _("E-mail field is required!"),
            },
            'phone': {
                'required': _("Phone field is required!"),
            },
            'education': {
                'required': _("Education field is required!"),
            },
            'dob': {
                'required': _("Date of birth is required!"),
            },
        }

        labels = {
            'email': "E-mail",
            'message': "What is in your mind?",
        }