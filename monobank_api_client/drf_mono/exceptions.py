from rest_framework import status
from rest_framework.exceptions import APIException


class MonoTokenDoesNotExistsException(APIException):
    status_code = status.HTTP_404_NOT_FOUND
    default_detail = "Monobank not added."
    default_code = "Monobank_not_added"


class MonoTokenExistsException(APIException):
    status_code = status.HTTP_400_BAD_REQUEST
    default_detail = "Monobank already added."
    default_code = "Monobank_already_added"
