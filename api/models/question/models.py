# -*- coding: utf-8 -*-
from django.db import models


class Question(models.Model):
    text = models.CharField(max_length=255, verbose_name="Вопрос")
    type_question = models.ForeignKey(
        "TypeQuestion",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        verbose_name="Тип вопроса"
    )
    user = models.ForeignKey("User", on_delete=models.CASCADE, verbose_name="Пользователь")

    def __str__(self):
        return f"{self.text} - {self.user.username}"

    @property
    def correct_answer(self):
        return self.answers_vote.get(is_current=True)

    class Meta:
        db_table = 'questions'  # Название таблицы в БД
        verbose_name = 'Вопрос'
        verbose_name_plural = 'Вопросы'
