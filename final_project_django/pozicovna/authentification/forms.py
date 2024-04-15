from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=300, help_text='Enter a valid email address')
    first_name = forms.CharField(max_length=50, help_text='Enter your first and optionally any middle names')
    last_name = forms.CharField(max_length=25, help_text='Enter your last name')

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', 'first_name', 'last_name')
