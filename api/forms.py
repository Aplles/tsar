# -*- coding: utf8 -*-
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django import forms
from django.contrib.auth import get_user_model


User = get_user_model()


class RegisterUserForm(UserCreationForm):
    username = forms.CharField(label='Логин', max_length=255,
                               widget=forms.TextInput(attrs={'id': 'textArea', 'class': 'login'}))
    password1 = forms.CharField(label='Пароль', required=False,
                                widget=forms.PasswordInput(
                                    attrs={"cols": 40, "rows": 6, 'id': 'textArea', 'class': 'password'}))
    password2 = forms.CharField(label='Повтор пароля', required=False,
                                widget=forms.PasswordInput(
                                    attrs={"cols": 40, "rows": 6, 'id': 'textArea', 'class': 'password'}))

    class Meta:
        model = User
        fields = ("username", 'password1', 'password2')


class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label='Почта', max_length=255,
                               widget=forms.TextInput(attrs={'id': 'textArea', 'class': 'login', 'type': 'email'}))
    password = forms.CharField(label='Пароль',
                               widget=forms.PasswordInput(
                                   attrs={"cols": 40, "rows": 6, 'id': 'textArea', 'class': 'password'}))


