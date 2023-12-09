from django.urls import path

from api_books.views.user import (
    UserLoginView,
    UserSendMailView,
    UserAuthView
)
from api_books.views.verdict import (
    BookListView,
    VerdictListView
)

urlpatterns = [
    # Verdict
    path("verdicts/", VerdictListView.as_view()),
    path('verdicts/<int:id>/books/', BookListView.as_view()),

    # User
    path('users/login/', UserLoginView.as_view()),
    path('users/send_mail/', UserSendMailView.as_view()),
    path('users/auth/', UserAuthView.as_view()),
]
