from django.urls import path

from api.views import MainPageView, UserLoginView, UserRegisterView, logout_user, VoteListCreateView

urlpatterns = [
    path('', MainPageView.as_view(), name="index"),
    path('votes/', VoteListCreateView.as_view(), name="vote"),
    path('user/login/', UserLoginView.as_view(), name="login"),
    path('user/register/', UserRegisterView.as_view(), name="register"),
    path('user/logout/', logout_user, name="logout"),
]
