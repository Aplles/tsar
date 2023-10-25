# -*- coding: utf-8 -*-
from django.db import models


class Text(models.Model):
    text = models.TextField(verbose_name="Текст")
    user = models.ForeignKey("User", on_delete=models.CASCADE, verbose_name="Пользователь")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата обновления')

    class Meta:
        db_table = 'texts'  # Название таблицы в БД
        verbose_name = 'Текст пользователя'
        verbose_name_plural = 'Текста пользователя'
