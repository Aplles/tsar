from service_objects.services import Service
from django import forms
from api.models import Verdict
from rest_framework.exceptions import NotFound


class BookListServices(Service):
    id = forms.IntegerField()

    def process(self):
        self.result = self._verdict.books_verdict.all()
        return self

    @property
    def _verdict(self) -> Verdict:
        try:
            return Verdict.objects.get(id=self.cleaned_data['id'])
        except Verdict.DoesNotExist:
            raise NotFound("Verdict with this ID not found")

