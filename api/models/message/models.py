# -*- coding: utf-8 -*-
from django.db import models


class Message(models.Model):
    text = models.TextField(verbose_name="Текст")
    user = models.ForeignKey("User", on_delete=models.CASCADE, verbose_name="Пользователь")
    author = models.ForeignKey(
        "User",
        on_delete=models.CASCADE,
        related_name='messages_user',
        verbose_name="Автор сообщения"
    )

    class Meta:
        db_table = 'messages'  # Название таблицы в БД
        verbose_name = 'Сообщение'
        verbose_name_plural = 'Сообщения'
