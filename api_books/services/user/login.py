from functools import lru_cache

from django import forms
from service_objects.services import Service
from rest_framework.exceptions import NotFound, PermissionDenied
from api.models.user.models import User


class UserLoginService(Service):
    email = forms.CharField()
    password = forms.CharField()

    def process(self):
        self.result = self._login()
        return self

    @property
    @lru_cache
    def _user(self):
        try:
            return User.objects.get(email=self.cleaned_data['email'])
        except User.DoesNotExist:
            raise NotFound("User with this login NotFound")

    def _login(self):
        if self._user.check_password(self.cleaned_data['password']):
            return self._user
        raise PermissionDenied("Invalid password")
