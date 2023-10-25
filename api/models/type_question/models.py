# -*- coding: utf-8 -*-
from django.db import models


class TypeQuestion(models.Model):
    title = models.CharField(max_length=255, verbose_name="Тип вопроса")

    def __str__(self):
        return f"{self.title}"

    class Meta:
        db_table = 'type_questions'  # Название таблицы в БД
        verbose_name = 'Тип вопроса'
        verbose_name_plural = 'Типы вопроса'
