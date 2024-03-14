from typing import Dict
from rest_framework.generics import GenericAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Mono
from .serializers import (
    MonoTokenSerializer,
    WebhookSerializer,
    MonoPeriodSerializer,
    MonoCurrencySerializer,
)
from sync_mono.manager import SyncMonoManager


class MonoView(GenericAPIView):
    serializer_class = MonoTokenSerializer

    def post(self, request) -> Dict:
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid()
        _ = serializer.validated_data
        mono = Mono.objects.filter(user=self.request.user)
        mng = SyncMonoManager()
        if mono.first() is not None:
            response = mng.exists_exception()
        else:
            mono.create(mono_token=_["mono_token"], user=request.user)
            response = mng.create_success()
        return Response(response)

    def put(self, request) -> Dict:
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        _ = serializer.validated_data
        mono = Mono.objects.filter(user=request.user)
        mng = SyncMonoManager()
        if mono.first() is not None:
            mono.update(mono_token=_["mono_token"])
            response = mng.update_success()
        else:
            response = mng.does_not_exsists_exception()
        return Response(response)

    def delete(self, request) -> Dict:
        mng = SyncMonoManager()
        mono = Mono.objects.filter(user=request.user)
        if mono.first() is not None:
            mono.delete()
            response = mng.delete_success()
        else:
            response = mng.does_not_exsists_exception()
        return Response(response)


class CurrenciesListView(APIView):
    def get(self, request) -> Dict:
        mng = SyncMonoManager()
        response = mng.get_currencies()
        return Response(response)


class CurrencyView(GenericAPIView):
    serializer_class = MonoCurrencySerializer

    def post(self, request) -> Dict:
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        currency = serializer.validated_data
        ccy_pair = currency.get("currency")
        mng = SyncMonoManager()
        response = mng.get_currency(ccy_pair)
        return Response(response)


class ClientInfoView(APIView):
    def get(self, request) -> Dict:
        mng = SyncMonoManager()
        mono = Mono.objects.filter(user=request.user).first()
        if mono is not None:
            mng.token = mono.mono_token
            response = mng.get_client_info()
        else:
            response = mng.does_not_exsists_exception()
        return Response(response)


class BalanceView(APIView):
    def get(self, request) -> Dict:
        mng = SyncMonoManager()
        mono = Mono.objects.filter(user=request.user).first()
        if mono is not None:
            mng.token = mono.mono_token
            response = mng.get_balance()
        else:
            response = mng.does_not_exsists_exception()
        return Response(response)


class StatementView(GenericAPIView):
    serializer_class = MonoPeriodSerializer

    def post(self, request) -> Dict:
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        _ = serializer.validated_data
        mng = SyncMonoManager()
        mono = Mono.objects.filter(user=request.user).first()
        if mono is not None:
            mng.token = mono.mono_token
            response = mng.get_statement(_["period"])
        else:
            response = mng.does_not_exsists_exception()
        return Response(response)


class CreateWebhook(GenericAPIView):
    serializer_class = WebhookSerializer

    def post(self, request) -> Dict:
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        _ = serializer.validated_data
        mng = SyncMonoManager()
        mono = Mono.objects.filter(user=request.user).first()
        if mono is not None:
            mng.token = mono.mono_token
            response = mng.create_webhook(_["webHookUrl"])
        else:
            response = mng.does_not_exsists_exception()
        return Response(response)
