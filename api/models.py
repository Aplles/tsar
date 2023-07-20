# -*- coding: utf-8 -*-

# Импорт нужных классов
from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):  # Создание класса Пользователя и наследуемся от AbstractUser

    def __str__(self):  # Магический метод __str__, который отображает объект в красивом виде
        return self.username

    class Meta:  # Мета класс
        db_table = 'users'  # Название таблицы в БД
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'


class HandWriting(models.Model):  # Создание класса Подписи и наследуемся от models.Model
    # Объявление полей в таблице
    symbol = models.CharField(max_length=255, verbose_name="Символ")
    performance = models.TextField(verbose_name="16 представление")
    binary = models.TextField(verbose_name="Бинарное представление")
    user = models.ForeignKey("User", on_delete=models.CASCADE, verbose_name="Пользователь")

    def __str__(self):
        return f"{self.symbol} - {self.performance} - {self.user.username}"

    class Meta:
        db_table = 'hand_writings'  # Название таблицы в БД
        verbose_name = 'Почерк'
        verbose_name_plural = 'Почерки'


class BinaryDict(models.Model):
    symbol = models.CharField(max_length=255, verbose_name="Символ")
    binary = models.CharField(max_length=255, verbose_name="Бинарное представление")

    def __str__(self):
        return f"{self.symbol} -- | -- {self.binary}"

    class Meta:
        db_table = 'binary_dicts'  # Название таблицы в БД
        ordering = ('symbol',)
        verbose_name = 'Бинари'
        verbose_name_plural = 'Бинари'


class TypeAnswer(models.Model):  # 4
    title = models.CharField(max_length=255, verbose_name="Тип вопроса")

    def __str__(self):
        return f"{self.title}"

    class Meta:
        db_table = 'type_answers'  # Название таблицы в БД
        verbose_name = 'Тип ответа'
        verbose_name_plural = 'Типы ответов'


class Question(models.Model):  # 2
    text = models.CharField(max_length=255, verbose_name="Вопрос")
    user = models.ForeignKey("User", on_delete=models.CASCADE, verbose_name="Пользователь")

    def __str__(self):
        return f"{self.text} - {self.user.username}"

    class Meta:
        db_table = 'questions'  # Название таблицы в БД
        verbose_name = 'Вопрос'
        verbose_name_plural = 'Вопросы'


class Answer(models.Model):  # 3
    text = models.CharField(max_length=255, verbose_name="Ответ")
    is_current = models.BooleanField(default=False, verbose_name="Правильный ли ответ?")
    type_answer = models.ForeignKey("TypeAnswer", on_delete=models.CASCADE, verbose_name="Тип ответа")
    vote = models.ForeignKey("Question", on_delete=models.CASCADE, verbose_name="вопрос")

    def __str__(self):
        return f"{self.text} - {self.is_current}"

    class Meta:
        db_table = 'answers'  # Название таблицы в БД
        verbose_name = 'Ответ'
        verbose_name_plural = 'Ответы'
