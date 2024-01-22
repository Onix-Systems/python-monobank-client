from rest_framework.generics import GenericAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Mono
from .serializers import (
    MonoTokenSerializer,
    WebhookSerializer,
    MonoPeriodSerializer,
    MonoCurrencySerializer,
)
from .exceptions import (
    MonoTokenExistsException,
    MonoTokenDoesNotExistsException,
)

from sync_mono.manager import SyncMonoManager


class MonoView(GenericAPIView):
    serializer_class = MonoTokenSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        _ = serializer.validated_data
        mono_obj = Mono.objects.filter(user=self.request.user)
        if mono_obj.first() is not None:
            raise MonoTokenExistsException
        mono_obj.create(mono_token=_["mono_token"], user=request.user)
        return Response(
            {"detail": "Monobank added successfully."}, status.HTTP_201_CREATED
        )

    def put(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        _ = serializer.validated_data
        mono_obj = Mono.objects.filter(user=request.user)
        if mono_obj.first() is not None:
            mono_obj.update(mono_token=_["mono_token"])
            return Response({"detail": "Monobank changed successfully."})
        raise MonoTokenDoesNotExistsException

    def delete(self, request):
        mono_obj = Mono.objects.filter(user=request.user)
        if mono_obj.first() is not None:
            mono_obj.delete()
            return Response(status.HTTP_204_NO_CONTENT)
        raise MonoTokenDoesNotExistsException


class CurrenciesListView(APIView):
    def get(self, request):
        mng = SyncMonoManager()
        response = mng.get_currencies()
        return Response(response)


class CurrencyView(GenericAPIView):
    serializer_class = MonoCurrencySerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        currency = serializer.validated_data
        ccy_pair = currency.get("currency")
        mng = SyncMonoManager()
        response = mng.get_currency(ccy_pair)
        return Response(response)


class ClientInfoView(APIView):
    def get(self, request):
        mono_obj = Mono.objects.filter(user=request.user).first()
        if mono_obj is not None:
            mng = SyncMonoManager(mono_obj.mono_token)
            response = mng.get_client_info()
            return Response(response)
        raise MonoTokenDoesNotExistsException


class BalanceView(APIView):
    def get(self, request):
        mono_obj = Mono.objects.filter(user=request.user).first()
        if mono_obj is not None:
            mng = SyncMonoManager(mono_obj.mono_token)
            response = mng.get_balance()
            return Response(response)
        raise MonoTokenDoesNotExistsException


class StatementView(GenericAPIView):
    serializer_class = MonoPeriodSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        _ = serializer.validated_data
        mono_obj = Mono.objects.filter(user=request.user).first()
        if mono_obj is not None:
            mng = SyncMonoManager(mono_obj.mono_token)
            response = mng.get_statement(_["period"])
            return Response(response)
        raise MonoTokenDoesNotExistsException


class CreateWebhook(GenericAPIView):
    serializer_class = WebhookSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        _ = serializer.validated_data
        mono_obj = Mono.objects.filter(user=request.user).first()
        if mono_obj is not None:
            mng = SyncMonoManager(mono_obj.mono_token)
            response = mng.create_webhook(_["webHookUrl"])
            return Response(response)
        raise MonoTokenDoesNotExistsException
