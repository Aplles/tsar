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
    TextDeleteView,
    VoteListResultView,
    EmailShowView,
    MessageUploadView,
    UserFinanceView,
)

urlpatterns = [
    path('', MainPageView.as_view(), name="index"),
    path('votes/', VoteListCreateView.as_view(), name="vote"),
    path('votes/result/', VoteListResultView.as_view(), name="vote_result"),
    path('user/login/', UserLoginView.as_view(), name="login"),
    path('user/register/', UserRegisterView.as_view(), name="register"),
    path('user/logout/', logout_user, name="logout"),

    path("send/", EmailSendView.as_view(), name='send'),
    path("mail/", EmailShowView.as_view(), name='email'),
    path("mail/<int:id>/upload", MessageUploadView.as_view(), name='upload_message'),
    path("upload_symbol/", UploadSymbolView.as_view(), name='upload_symbol'),


    path("text/", TextCreateView.as_view(), name='index_text'),
    path("text/<int:id>/upload", TextUploadView.as_view(), name='upload_text'),
    path("text/<int:id>/delete", TextDeleteView.as_view(), name='delete_text'),
    path("profile/", UserProfileView.as_view(), name='profile'),
    path("profile/finance", UserFinanceView.as_view(), name='finance'),
]
