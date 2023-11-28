# -*- coding: utf-8 -*-
from django.db import models


class UserAnswer(models.Model):
    question = models.ForeignKey(
        "Question",
        on_delete=models.CASCADE,
        verbose_name="вопрос",
        related_name='questions_user'
    )
    answer = models.ForeignKey("Answer", on_delete=models.CASCADE, verbose_name="Ответ")
    user = models.ForeignKey("User", on_delete=models.CASCADE, verbose_name="Пользователь")

    def __str__(self):
        return f"{self.question} - {self.answer} - {self.user}"

    class Meta:
        db_table = 'user_answers'  # Название таблицы в БД
        verbose_name = 'Ответ пользователя'
        verbose_name_plural = 'Ответы пользователя'
