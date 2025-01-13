from typing import Dict
from rest_framework.generics import GenericAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from monobank_api_client.drf_mono.models import Mono
from monobank_api_client.drf_mono.serializers import (
    MonoTokenSerializer,
    WebhookSerializer,
    MonoPeriodSerializer,
    MonoCurrencySerializer,
)
from monobank_api_client.sync_mono.manager import SyncMonoManager


class MonoView(GenericAPIView):
    """
    Handles operations related to Mono tokens such as creation, update, and deletion.

    Methods:
        post: Create a Mono token.
        put: Update a Mono token.
        delete: Delete a Mono token.

    """
    serializer_class = MonoTokenSerializer

    def post(self, request) -> Dict:
        """
        Create a Mono token for the current user.

        :param request: The HTTP request containing the token data.
        :returns: A response indicating success or if the token already exists.
        """
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
        """
        Update the Mono token for the current user.

        :param request: The HTTP request containing updated token data.
        :returns: A response indicating success or if the token was not found.
        """
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
        """
        Delete the Mono token for the current user.

        :param request: The HTTP request.
        :returns: A response indicating success or if the token was not found.
        """
        mng = SyncMonoManager()
        mono = Mono.objects.filter(user=request.user)
        if mono.first() is not None:
            mono.delete()
            response = mng.delete_success()
        else:
            response = mng.does_not_exsists_exception()
        return Response(response)


class CurrenciesListView(APIView):
    """
    Provides a list of available currencies via a GET request.
    """

    def get(self, request) -> Dict:
        """
        Retrieve a list of available currencies.

        :param request:The HTTP request.
        :returns: A response containing the currencies list.
        """
        mng = SyncMonoManager()
        response = mng.get_currencies()
        return Response(response)


class CurrencyView(GenericAPIView):
    """
    Retrieves details about a specific currency based on a provided currency pair.

    Methods:
        - post: Get details for a specific currency by currency pair.
    """
    serializer_class = MonoCurrencySerializer

    def post(self, request) -> Dict:
        """
        Retrieve information for a specific currency.

        :param request: The HTTP request containing the currency pair data.
        :returns: A response with the currency details.
        """
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        currency = serializer.validated_data
        ccy_pair = currency.get("currency")
        mng = SyncMonoManager()
        response = mng.get_currency(ccy_pair)
        return Response(response)


    """
    Retrieves client information based on the Mono token via a GET request.
    """

    def get(self, request) -> Dict:
        """
        Retrieve client information using the Mono token.

        :param request: The HTTP request.

        :returns: A response with client details or an error if no token is found.
        """
        mng = SyncMonoManager()
        mono = Mono.objects.filter(user=request.user).first()
        if mono is not None:
            mng.token = mono.mono_token
            response = mng.get_client_info()
        else:
            response = mng.does_not_exsists_exception()
        return Response(response)


class BalanceView(APIView):
    """
    Retrieves the balance information for the current user based on the Mono token.
    """
    def get(self, request) -> Dict:
        """
        Retrieve the account balance for the current user.

        :param request: The HTTP request.
        :returns: A response with the account balance or an error if the token is not found.
        """
        mng = SyncMonoManager()
        mono = Mono.objects.filter(user=request.user).first()
        if mono is not None:
            mng.token = mono.mono_token
            response = mng.get_balance()
        else:
            response = mng.does_not_exsists_exception()
        return Response(response)


class StatementView(GenericAPIView):
    """
    Generates account statements based on a specific period via a POST request.
    """

    serializer_class = MonoPeriodSerializer

    def post(self, request) -> Dict:
        """
        Retrieve account statements for a specified period.

        :param request: The HTTP request containing the period data.
        :returns: A response with the account statements or an error if the token is not found.
        """
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
    """
    Creates webhooks for the Mono service via a POST request.
    """

    serializer_class = WebhookSerializer

    def post(self, request) -> Dict:
        """
        Create a webhook for the current user's Mono configuration.

        :param request: The HTTP request containing the webhook URL data.
        :returns: A response indicating success or an error if no token is found.
        """
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
