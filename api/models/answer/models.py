# -*- coding: utf-8 -*-
from django.db import models


class Answer(models.Model):  # 3
    text = models.CharField(max_length=255, verbose_name="Ответ")
    is_current = models.BooleanField(default=False, verbose_name="Правильный ли ответ?")
    argument = models.TextField(null=True, blank=True, verbose_name="Аргумент")
    type_answer = models.ForeignKey("TypeAnswer", on_delete=models.CASCADE, verbose_name="Тип ответа")
    vote = models.ForeignKey("Question", on_delete=models.CASCADE, verbose_name="вопрос", related_name='answers_vote')

    def __str__(self):
        return f"{self.text} - {self.is_current}"

    class Meta:
        db_table = 'answers'  # Название таблицы в БД
        verbose_name = 'Ответ'
        verbose_name_plural = 'Ответы'