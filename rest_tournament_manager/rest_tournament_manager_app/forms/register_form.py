from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.utils.datetime_safe import datetime

BIRTH_YEAR_CHOICES = ['1980', '1981', '1982']


class RegisterForm(UserCreationForm):
    email = forms.EmailField()
    birth_date = forms.DateField(
        widget=forms.SelectDateWidget(years=range(datetime.now().year - 100, datetime.now().year - 10)))

    class Meta:
        model = User
        fields = ["username", 'birth_date', "email", "password1", "password2"]
