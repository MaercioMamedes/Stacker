from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from core.models import CarStack
from core.serializer import CarSerializer
from core.helpers import authenticator, get_stack

"""View da pilha de carros no pátio"""


class CarsListStackView(GenericAPIView):
    serializer_class = CarSerializer
    """Retorna todos os carros cadastrados na pliha, ordenados de forma decrescente em relação a data e hora de entrada"""
    queryset = CarStack.objects.all().order_by('-input_in')

    def get(self, request):

        if authenticator(self.request):

            return Response(get_stack(self.get_queryset()))  # retorna pilha formatada

        else:
            return Response(
                {
                    'msg': 'chave inválida'
                },
                status=401)
