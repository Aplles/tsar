# -*- coding: utf-8 -*-
from django.db import models


class Balance(models.Model):
    balance = models.DecimalField(max_digits=19, decimal_places=3, default=0.0, verbose_name='Баланс')
    user = models.ForeignKey("User", on_delete=models.CASCADE, verbose_name="Пользователь")

    def __str__(self):
        return f'{self.user.username} - {self.balance}'

    class Meta:
        db_table = 'balance'  # Название таблицы в БД
        verbose_name = 'Баланс'
        verbose_name_plural = 'Балансы'
