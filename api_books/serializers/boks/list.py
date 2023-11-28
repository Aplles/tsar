from rest_framework import serializers
from api.models import Book


class BookListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Book
        fields = "__all__"
