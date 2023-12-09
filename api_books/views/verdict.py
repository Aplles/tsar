from rest_framework.response import Response
from rest_framework.views import APIView
from api.models import Verdict
from api_books.serializers.boks.list import BookListSerializer

from api_books.serializers.verdicts.list import VerdictListSerializer
from api_books.services.books.list import BookListServices


class VerdictListView(APIView):

    def get(self, request, *args, **kwargs):
        return Response(
            VerdictListSerializer(
                Verdict.objects.all(), many=True
            ).data
        )


class BookListView(APIView):

    def get(self, request, *args, **kwargs):
        outcome = BookListServices.execute(kwargs)
        return Response(
            BookListSerializer(
                outcome.result, many=True
            ).data
        )
