from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework_api_key.models import APIKey
from core.models import CarStack
from core.helpers import authenticator


class StackPopCar(APIView):

    def get(self, request):
        if authenticator(self.request):

            stack = CarStack.objects.all().order_by('-input_in')
            stack[0].delete()
            stack[0].save()

            return Response({'msg':'carro removido com sucesso'}, status=200)

        else:

            return Response({'detail':'Chave inválida'}, status=401)
