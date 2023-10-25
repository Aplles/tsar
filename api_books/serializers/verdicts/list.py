from rest_framework import serializers
from api.models import Verdict


class VerdictListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Verdict
        fields = "__all__"
