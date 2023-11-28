# -*- coding: utf-8 -*-
from django.db import models


class BinaryDict(models.Model):
    symbol = models.CharField(max_length=255, verbose_name="Символ")
    binary = models.CharField(max_length=255, verbose_name="Бинарное представление")

    def __str__(self):
        return f"{self.symbol} -- | -- {self.binary}"

    class Meta:
        db_table = 'binary_dicts'  # Название таблицы в БД
        ordering = ('symbol',)
        verbose_name = 'Бинари'
        verbose_name_plural = 'Бинари'
