from django.urls import path

from api.views import (
    MainPageView,
    UserLoginView,
    UserRegisterView,
    logout_user,
    VoteListCreateView,
    EmailSendView,
    UploadSymbolView,
    TextCreateView,
    UserProfileView,
    TextUploadView,
)

urlpatterns = [
    path('', MainPageView.as_view(), name="index"),
    path('votes/', VoteListCreateView.as_view(), name="vote"),
    path('user/login/', UserLoginView.as_view(), name="login"),
    path('user/register/', UserRegisterView.as_view(), name="register"),
    path('user/logout/', logout_user, name="logout"),

    path("send/", EmailSendView.as_view(), name='send'),
    path("upload_symbol/", UploadSymbolView.as_view(), name='upload_symbol'),


    path("text/", TextCreateView.as_view(), name='index_text'),
    path("text/upload", TextUploadView.as_view(), name='upload_text'),
    path("profile/", UserProfileView.as_view(), name='profile'),
]
