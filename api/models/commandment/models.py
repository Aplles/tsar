# -*- coding: utf-8 -*-
from django.db import models


class Commandment(models.Model):
    text = models.TextField(verbose_name="Текст")

    class Meta:
        db_table = 'commandments'
        verbose_name = 'Заповедь'
        verbose_name_plural = 'Заповеди'

    def __str__(self):
        return f'{self.text}'
