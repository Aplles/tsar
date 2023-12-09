from rest_framework.response import Response
from rest_framework.views import APIView
from api_books.serializers.user.show import UserSerializer
from api_books.services.user.login import UserLoginService
from rest_framework.permissions import IsAuthenticated


class UserLoginView(APIView):

    def post(self, request, *args, **kwargs):
        outcome = UserLoginService.execute(request.POST)
        return Response(UserSerializer(outcome.result).data)


class UserSendMailView(APIView):
    def post(self, request, *args, **kwargs):
        pass


class UserAuthView(APIView):
    permission_classes = [IsAuthenticated, ]

    def post(self, request, *args, **kwargs):
        return Response(UserSerializer(request.user).data)
