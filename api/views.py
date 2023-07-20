import random

from django.contrib.auth import logout, login
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import CreateView

from .forms import RegisterUserForm, LoginUserForm
from .models import HandWriting, BinaryDict


# Create your views here.
class MainPageView(View):
    LINE_SYMBOL = '1234567890-=qwertyuiop[]asdfghjkl;zxcvbnm,./~!@#$%^&*()_+QWERTYUIOP{}ASDFGHJKL:"ZXCVBNM<>?'

    @classmethod
    def random_hex(cls):
        result = ""
        for i in range(16):
            result += cls.LINE_SYMBOL[random.randint(0, len(cls.LINE_SYMBOL) - 1)]
        return result

    def get(self, request, *args, **kwargs):
        return render(request, "index.html", context={

        })

    def post(self, request, *args, **kwargs):
        symbol = request.POST['symbol']
        if HandWriting.objects.filter(symbol=symbol):
            return redirect('index')
        binary = ""
        performance = self.random_hex()
        for symbol_performance in performance:
            binary += BinaryDict.objects.get(symbol=symbol_performance).binary
        HandWriting.objects.create(
            symbol=symbol,
            performance=performance,
            binary=binary,
            user=request.user
        )
        return redirect('index')


def logout_user(request):
    """Log out"""
    logout(request)
    return redirect('index')


class UserRegisterView(CreateView):
    form_class = RegisterUserForm
    template_name = 'register.html'
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('index')


class UserLoginView(LoginView):
    form_class = LoginUserForm
    template_name = 'login.html'

    def get_success_url(self):
        return reverse_lazy('index')


class VoteListCreateView(View):

    def get(self, request, *args, **kwargs):
        return render(request, "vote.html")
