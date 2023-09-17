# -*- coding: utf-8 -*-

# Импорт нужных классов
from django.contrib.auth.models import AbstractUser
from django.db import models


class Role(models.Model):
    role = models.CharField(max_length=255, unique=True, verbose_name="Роль")
    description = models.TextField(verbose_name="Описание роли")

    class Meta:  # Мета класс
        db_table = 'roles'  # Название таблицы в БД
        verbose_name = 'Роль'
        verbose_name_plural = 'Роли'


class User(AbstractUser):  # Создание класса Пользователя и наследуемся от AbstractUser
    role = models.ForeignKey(
        Role,
        on_delete=models.CASCADE,
        verbose_name="Роль",
        null=True,
        blank=True
    )
    username = models.CharField(
        max_length=255,
        verbose_name="Логин",
        null=True,
        blank=True
    )
    ip_address = models.CharField(max_length=255, verbose_name="Ip-адресс")
    email = models.EmailField(unique=True, verbose_name='почта')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):  # Магический метод __str__, который отображает объект в красивом виде
        return self.username

    class Meta:  # Мета класс
        db_table = 'users'  # Название таблицы в БД
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'


class Code(models.Model):
    code = models.CharField(max_length=6, verbose_name="Код пользователя")
    email = models.CharField(max_length=255, verbose_name="Почта")

    def __str__(self):
        return f"{self.code} - {self.email}"


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

    @property
    def correct_answer(self):
        return self.answers_vote.get(is_current=True)

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
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата обновления')

    class Meta:
        db_table = 'texts'  # Название таблицы в БД
        verbose_name = 'Текст пользователя'
        verbose_name_plural = 'Текста пользователя'


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


class Balance(models.Model):
    balance = models.DecimalField(max_digits=19, decimal_places=3, default=0.0, verbose_name='Баланс')
    user = models.ForeignKey("User", on_delete=models.CASCADE, verbose_name="Пользователь")

    def __str__(self):
        return f'{self.user.username} - {self.balance}'

    class Meta:
        db_table = 'balance'  # Название таблицы в БД
        verbose_name = 'Баланс'
        verbose_name_plural = 'Балансы'


class Room(models.Model):
    user = models.ForeignKey("User", on_delete=models.CASCADE, verbose_name="Пользователь")
    is_public = models.BooleanField(default=False, verbose_name='Публичная ли комната?')

    def __str__(self):
        return f'Комната пользователя {self.user}'

    class Meta:
        db_table = 'rooms'
        verbose_name = 'Комната'
        verbose_name_plural = 'Комнаты'


class Commandment(models.Model):
    text = models.TextField(verbose_name="Текст")

    class Meta:
        db_table = 'commandments'
        verbose_name = 'Заповедь'
        verbose_name_plural = 'Заповеди'

    def __str__(self):
        return f'{self.text}'


class Verdict(models.Model):
    text = models.TextField(verbose_name="Текст")

    class Meta:
        db_table = 'verdicts'
        verbose_name = 'Вердикт'
        verbose_name_plural = 'Вердикты'

    def __str__(self):
        return f'{self.text}'


class Book(models.Model):
    text = models.TextField(verbose_name="Текст")
    verdict = models.ForeignKey(Verdict, on_delete=models.CASCADE, verbose_name='Вердикт')

    class Meta:
        db_table = 'books'
        verbose_name = 'Книга'
        verbose_name_plural = 'Книги'

    def __str__(self):
        return f'{self.text}'


class BookMember(models.Model):
    name = models.TextField(verbose_name="Имя")
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='members_book', verbose_name='Книга')

    class Meta:
        db_table = 'book_members'
        verbose_name = 'Участник книги'
        verbose_name_plural = 'Участники книги'

    def __str__(self):
        return f'{self.name} - {self.book}'
