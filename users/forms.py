from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    # this class gives the nested namespace for configurations and keeps them in one place
    # the model that is going to be affected is User model
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
