# -*- coding: utf-8 -*-
from django.db import models


class Room(models.Model):
    user = models.ForeignKey("User", on_delete=models.CASCADE, verbose_name="Пользователь")
    is_public = models.BooleanField(default=False, verbose_name='Публичная ли комната?')

    def __str__(self):
        return f'Комната пользователя {self.user}'

    class Meta:
        db_table = 'rooms'
        verbose_name = 'Комната'
        verbose_name_plural = 'Комнаты'
