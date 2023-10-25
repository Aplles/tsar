# -*- coding: utf-8 -*-
from django.db import models


class Role(models.Model):
    role = models.CharField(max_length=255, unique=True, verbose_name="Роль")
    description = models.TextField(verbose_name="Описание роли")

    class Meta:  # Мета класс
        db_table = 'roles'  # Название таблицы в БД
        verbose_name = 'Роль'
        verbose_name_plural = 'Роли'