from django.contrib.auth.models import AbstractUser
# -*- coding: utf-8 -*-
from django.db import models


class User(AbstractUser):  # Создание класса Пользователя и наследуемся от AbstractUser
    role = models.ForeignKey(
        'Role',
        on_delete=models.CASCADE,
        verbose_name="Роль",
        null=True,
        blank=True
    )
    username = models.CharField(
        max_length=255,
        verbose_name="Логин",
        null=True,
        blank=True
    )
    ip_address = models.CharField(max_length=255, verbose_name="Ip-адресс")
    email = models.EmailField(unique=True, verbose_name='почта')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):  # Магический метод __str__, который отображает объект в красивом виде
        return self.username

    class Meta:  # Мета класс
        db_table = 'users'  # Название таблицы в БД
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'