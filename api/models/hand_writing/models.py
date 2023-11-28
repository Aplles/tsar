# -*- coding: utf-8 -*-
from django.db import models


class HandWriting(models.Model):
    symbol = models.CharField(max_length=255, verbose_name="Символ")
    performance = models.TextField(verbose_name="16 представление")
    binary = models.TextField(verbose_name="Бинарное представление")
    user = models.ForeignKey("User", on_delete=models.CASCADE, verbose_name="Пользователь")

    def __str__(self):
        return f"{self.symbol} - {self.performance} - {self.user.username}"

    class Meta:
        db_table = 'hand_writings'  # Название таблицы в БД
        verbose_name = 'Почерк'
        verbose_name_plural = 'Почерки'
