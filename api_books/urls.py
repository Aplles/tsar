from django.urls import path

from api_books.views import (
    BookListView,
    VerdictListView
)

urlpatterns = [
    path("verdicts/", VerdictListView.as_view()),
    path('verdicts/<int:id>/books/', BookListView.as_view()),
]
