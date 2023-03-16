from rest_framework.views import APIView
from rest_framework.response import Response
from core.models import CarStack
from core.helpers import authenticator

"""View para remover carro da pilha"""


class StackPopCar(APIView):

    def get(self, request):
        if authenticator(self.request):

            """Retorna todos os carros cadastrados na pliha, ordenados de forma decrescente em relação a data e hora de entrada"""
            stack = CarStack.objects.all().order_by('-input_in')

            stack[0].car.delete()  # retira primeiro carro da pilha

            return Response({'msg':'carro removido com sucesso'}, status=200)

        else:

            return Response({'detail':'Chave inválida'}, status=401)
