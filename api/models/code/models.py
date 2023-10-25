# -*- coding: utf-8 -*-
from django.db import models


class Code(models.Model):
    code = models.CharField(max_length=6, verbose_name="Код пользователя")
    email = models.CharField(max_length=255, verbose_name="Почта")

    def __str__(self):
        return f"{self.code} - {self.email}"
