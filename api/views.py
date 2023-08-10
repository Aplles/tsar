import csv
import random
import smtplib
from email.mime.text import MIMEText
from email.header import Header
from functools import lru_cache

import openpyxl
from django.contrib.auth import logout, login
from django.contrib.auth.views import LoginView
from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import CreateView, TemplateView

from .forms import RegisterUserForm, LoginUserForm
from .models import BinaryDict, HandWriting, Question, Answer, UserAnswer, Text, User, Message, Balance


class MainPageView(View):

    def get(self, request, *args, **kwargs):
        return render(request, "index.html", context={
            'index': True
        })


def logout_user(request):
    """Log out"""
    logout(request)
    return redirect('index')


class UserRegisterView(CreateView):
    form_class = RegisterUserForm
    template_name = 'register.html'
    success_url = reverse_lazy('index')

    LINE_SYMBOL = '1234567890-=qwertyuiop[]asdfghjkl;zxcvbnm,./~!@#$%^&*()_+QWERTYUIOP{}ASDFGHJKL:"ZXCVBNM<>?'
    LIST_REQUIRED_SYMBOLS = ["", "'", "-", " ", "!", "\"", "#", "$", "%", "&", "(", ")", "*", ",", ".", "/", ":", ";",
                             "?", "@", "[", "]", "^", "_", "{", "|", "}", "~", "+", "<", ">", "0", "1", "2", "3",
                             "4", "5", "6", "7", "8", "9", "a", "A", "b", "B", "c", "C", "d", "D", "e", "E", "f", "F",
                             "g", "G", "h", "H", "i", "I", "j", "J", "k", "K", "l", "L", "m", "M", "n", "N", "o", "O",
                             "p", "P", "q", "Q", "r", "R", "s", "S", "t", "T", "u", "U", "v", "V", "w", "W", "x", "X",
                             "y", "Y", "z", "Z", "а", "А", "б", "Б", "в", "В", "г", "Г", "д", "Д", "е", "Е", "ё", "Ё",
                             "ж", "Ж", "з", "З", "и", "И", "й", "Й", "к", "К", "л", "Л", "м", "М", "н", "Н", "о", "О",
                             "п", "П", "р", "Р", "с", "С", "т", "Т", "у", "У", "ф", "Ф", "х", "Х", "ц", "Ц", "ч", "Ч",
                             "ш", "Ш", "щ", "Щ", "ъ", "Ъ", "ы", "Ы", "ь", "Ь", "э", "Э", "ю", "Ю", "я", "Я"]

    @classmethod
    def random_hex(cls):
        result = ""
        for i in range(30):
            result += cls.LINE_SYMBOL[random.randint(0, len(cls.LINE_SYMBOL) - 1)]
        return result

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        for symbol in self.LIST_REQUIRED_SYMBOLS:
            binary = ""
            performance = self.random_hex()
            for symbol_performance in performance:
                binary += BinaryDict.objects.get(symbol=symbol_performance).binary
            HandWriting.objects.create(
                symbol=symbol,
                performance=performance,
                binary=binary,
                user=user
            )
        Balance.objects.create(user=user)
        return redirect('profile')


class UserLoginView(LoginView):
    form_class = LoginUserForm
    template_name = 'login.html'

    def get_success_url(self):
        return reverse_lazy('profile')


class VoteListCreateView(View):

    def get(self, request, *args, **kwargs):
        return render(request, "vote.html", context={
            'questions': Question.objects.filter(questions_user__answer__isnull=True)
        })

    def post(self, request, *args, **kwargs):
        question = Question.objects.get(id=request.POST['question_id'])
        answer = Answer.objects.get(id=request.POST['answer_id'])
        UserAnswer.objects.create(
            question=question,
            answer=answer,
            user=request.user,
        )
        return redirect('vote')


class EmailSendView(View):

    def post(self, request, *args, **kwargs):
        mailsender = smtplib.SMTP('smtp.gmail.com', 587)
        mailsender.starttls()
        mailsender.login('imperiya66isa@gmail.com', 'hzrnhucrocxevivl')
        mail_recipient = 'david26121980@gmail.com'
        mail_subject = 'Тема сообщения'
        mail_body = 'Текст сообщения'
        msg = MIMEText(mail_body, 'plain', 'utf-8')
        msg['Subject'] = Header(mail_subject, 'utf-8')
        mailsender.sendmail('imperiya66isa@gmail.com', mail_recipient, msg.as_string())
        mailsender.quit()
        return redirect("index")


class UploadSymbolView(View):

    def post(self, request, *args, **kwargs):
        response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
        response['Content-Disposition'] = 'attachment; filename="hand_writing.xlsx"'
        workbook = openpyxl.Workbook()
        worksheet = workbook.active
        worksheet.title = 'Hand Writing Data'
        headers = ['Символ', 'Шестнадцатеричное', 'Бинарь']
        worksheet.append(headers)
        hand_writing = HandWriting.objects.filter(user=request.user)
        for symbol in hand_writing:
            data_row = [symbol.symbol, symbol.performance, symbol.binary]
            worksheet.append(data_row)

        workbook.save(response)
        return response


class TextCreateView(View):

    def post(self, request, *args, **kwargs):
        Text.objects.create(
            text=request.POST['text'],
            user=request.user
        )
        return redirect('profile')


class UserProfileView(View):

    def get(self, request, *args, **kwargs):
        return render(request, 'profile.html', context={
            'texts': Text.objects.filter(user=request.user).order_by('-created_at')
        })


class TextUploadView(View):

    def post(self, request, *args, **kwargs):
        response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
        response['Content-Disposition'] = 'attachment; filename="hand_writing.xlsx"'
        workbook = openpyxl.Workbook()
        worksheet = workbook.active
        worksheet.title = 'Выгрузка текста'
        headers = ['Символ', 'Шестнадцатеричное', 'Бинарь']
        worksheet.append(headers)
        text = Text.objects.get(id=kwargs['id']).text
        performance = "".join([self._hand_writings[symbol][0] for symbol in text])
        binary = "".join([self._hand_writings[symbol][1] for symbol in text])
        worksheet.append([text, performance, binary])
        workbook.save(response)
        return response

    @property
    @lru_cache
    def _hand_writings(self):
        hand_writings = HandWriting.objects.filter(
            user=self.request.user
        )
        return {
            hand_writing.symbol: [hand_writing.performance, hand_writing.binary]
            for hand_writing in hand_writings
        }


class TextDeleteView(View):

    def post(self, request, *args, **kwargs):
        Text.objects.get(
            id=kwargs['id'],
            user=request.user
        ).delete()
        return redirect('profile')


class VoteListResultView(View):

    def get(self, request, *args, **kwargs):
        user_answers = UserAnswer.objects.annotate(

        ).filter(user=request.user)
        return render(request, 'vote_result.html', context={
            'user_answers': user_answers
        })


class EmailShowView(View):

    def get(self, request, *args, **kwargs):
        return render(request, 'mail.html', context={
            'users': User.objects.filter(~Q(id=request.user.id)),
            'messages': Message.objects.filter(user=request.user)
        })

    def post(self, request, *args, **kwargs):
        text = request.POST.get("text_message")
        if not text:
            return redirect('email')
        Message.objects.create(
            text=text,
            user=User.objects.get(id=request.POST['user_id']),
            author=request.user
        )
        return redirect('email')


class MessageUploadView(View):

    def post(self, request, *args, **kwargs):
        response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
        response['Content-Disposition'] = 'attachment; filename="message.xlsx"'
        workbook = openpyxl.Workbook()
        worksheet = workbook.active
        worksheet.title = 'Выгрузка сообщения'
        headers = ['Символ', 'Шестнадцатеричное', 'Бинарь']
        worksheet.append(headers)
        message = Message.objects.get(id=kwargs['id']).text
        performance = "".join([self._hand_writings[symbol][0] for symbol in message])
        binary = "".join([self._hand_writings[symbol][1] for symbol in message])
        worksheet.append([message, performance, binary])
        workbook.save(response)
        return response

    @property
    @lru_cache
    def _hand_writings(self):
        hand_writings = HandWriting.objects.filter(
            user=self.request.user
        )
        return {
            hand_writing.symbol: [hand_writing.performance, hand_writing.binary]
            for hand_writing in hand_writings
        }


class UserFinanceView(View):

    def get(self, request, *args, **kwargs):
        return render(request, 'finance.html', context={
            'balance': Balance.objects.get(user=request.user).balance
        })


class UserKeyView(View):

    def get(self, request, *args, **kwargs):
        return render(request, 'keys.html', context={

        })


class EmailSentShowView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'list_sent_user.html', context={
            'sent_messages': Message.objects.filter(author=request.user)
        })


class StudyingShowView(View):

    def get(self, request, *args, **kwargs):
        return render(request, 'studying.html', context={
        })


class WorkShowView(View):

    def get(self, request, *args, **kwargs):
        return render(request, 'work.html', context={
        })


class MatrixPage(TemplateView):
    template_name = 'matrix.html'
