import csv
import random
import smtplib
from email.mime.text import MIMEText
from email.header import Header

import openpyxl
from django.contrib.auth import logout, login
from django.contrib.auth.views import LoginView
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import CreateView

from .forms import RegisterUserForm, LoginUserForm
from .models import BinaryDict, HandWriting


class MainPageView(View):

    def get(self, request, *args, **kwargs):
        return render(request, "index.html")


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
        return redirect('index')


class UserLoginView(LoginView):
    form_class = LoginUserForm
    template_name = 'login.html'

    def get_success_url(self):
        return reverse_lazy('index')


class VoteListCreateView(View):

    def get(self, request, *args, **kwargs):
        return render(request, "vote.html")


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
