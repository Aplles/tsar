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
    title = models.CharField(max_length=255, verbose_name="Тип ответа")

    def __str__(self):
        return f"{self.title}"

    class Meta:
        db_table = 'type_answers'  # Название таблицы в БД
        verbose_name = 'Тип ответа'
        verbose_name_plural = 'Типы ответов'


class TypeQuestion(models.Model):
    title = models.CharField(max_length=255, verbose_name="Тип вопроса")

    def __str__(self):
        return f"{self.title}"

    class Meta:
        db_table = 'type_questions'  # Название таблицы в БД
        verbose_name = 'Тип вопроса'
        verbose_name_plural = 'Типы вопроса'


class Question(models.Model):  # 2
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

    class Meta:
        db_table = 'questions'  # Название таблицы в БД
        verbose_name = 'Вопрос'
        verbose_name_plural = 'Вопросы'


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


class Text(models.Model):
    text = models.TextField(verbose_name="Текст")
    user = models.ForeignKey("User", on_delete=models.CASCADE, verbose_name="Пользователь")

    class Meta:
        db_table = 'texts'  # Название таблицы в БД
        verbose_name = 'Текст пользователя'
        verbose_name_plural = 'Текста пользователя'
