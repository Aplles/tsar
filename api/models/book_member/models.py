# -*- coding: utf-8 -*-
from django.db import models


class BookMember(models.Model):
    name = models.TextField(verbose_name="Имя")
    book = models.ForeignKey('Book', on_delete=models.CASCADE, related_name='members_book', verbose_name='Книга')

    class Meta:
        db_table = 'book_members'
        verbose_name = 'Участник книги'
        verbose_name_plural = 'Участники книги'

    def __str__(self):
        return f'{self.name} - {self.book}'
