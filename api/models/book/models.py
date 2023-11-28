# -*- coding: utf-8 -*-
from django.db import models


class Book(models.Model):
    text = models.TextField(verbose_name="Текст")
    image = models.ImageField(upload_to="book_images/", verbose_name="Изображение")
    slug = models.SlugField(unique=True, verbose_name="Слаг")
    verdict = models.ForeignKey('Verdict', on_delete=models.CASCADE, related_name='books_verdict', verbose_name='Вердикт')

    class Meta:
        db_table = 'books'
        verbose_name = 'Книга'
        verbose_name_plural = 'Книги'

    def __str__(self):
        return f'{self.text}'
