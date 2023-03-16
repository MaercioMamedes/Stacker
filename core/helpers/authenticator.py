from rest_framework_api_key.models import APIKey
from django.utils.datastructures import MultiValueDictKeyError

"""Função para atenticar API KEY da requisição"""


def authenticator(request):

    try:
        key = request.GET['api_key']
        api_key = APIKey.objects.get_from_key(key)
        return True

    except APIKey.DoesNotExist:

        return False

    except MultiValueDictKeyError:
        return False
