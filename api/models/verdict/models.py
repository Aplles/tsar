# -*- coding: utf-8 -*-
from django.db import models


class Verdict(models.Model):
    text = models.TextField(verbose_name="Текст")
    image = models.ImageField(upload_to="verdict_images/", verbose_name="Изображение")

    class Meta:
        db_table = 'verdicts'
        verbose_name = 'Вердикт'
        verbose_name_plural = 'Вердикты'

    def __str__(self):
        return f'{self.text}'
