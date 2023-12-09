from rest_framework import serializers
from api.models import User


class UserSerializer(serializers.ModelSerializer):
    token = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = (
            "id",
            "token",
            "email",
            "username",
            "role",
            "last_login",
            "is_superuser",
            "first_name",
            "last_name",
            "date_joined"
        )

    def get_token(self, obj):
        return obj.auth_token.key if hasattr(obj, 'auth_token') else None
