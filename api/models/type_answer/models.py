# -*- coding: utf-8 -*-
from django.db import models


class TypeAnswer(models.Model):  # 4
    title = models.CharField(max_length=255, verbose_name="Тип ответа")

    def __str__(self):
        return f"{self.title}"

    class Meta:
        db_table = 'type_answers'  # Название таблицы в БД
        verbose_name = 'Тип ответа'
        verbose_name_plural = 'Типы ответов'
