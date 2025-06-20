from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User

class UserRegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("username", "email", "phone_number", "role", "license_number", "password1", "password2")
        widgets = {
            'password1': forms.PasswordInput(),
            'role': forms.RadioSelect(choices=User.ROLE_CHOICES),
        }



    def __init__(self, *args, **kwargs):
        super(UserRegistrationForm, self).__init__(*args, **kwargs)
        # Remove 'admin' from role choices
        self.fields['role'].choices = [
            choice for choice in User.ROLE_CHOICES if choice[0] != User.ADMIN
        ]

class UserLoginForm(forms.Form):
    email = forms.EmailField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)

