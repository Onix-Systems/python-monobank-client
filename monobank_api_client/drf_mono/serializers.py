from rest_framework import serializers
from .models import Mono


class MonoTokenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mono
        fields = ["mono_token"]
        extra_kwargs = {"mono_token": {"write_only": True}}


class MonoPeriodSerializer(serializers.Serializer):
    period = serializers.IntegerField(min_value=0, max_value=31)


class WebhookSerializer(serializers.Serializer):
    webHookUrl = serializers.URLField()


class MonoCurrencySerializer(serializers.Serializer):
    currency = serializers.CharField()
