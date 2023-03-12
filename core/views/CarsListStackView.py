from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from core.models import CarStack
from core.serializer import CarSerializer
from core.helpers import authenticator


class CarsListStackView(GenericAPIView):
    serializer_class = CarSerializer

    def get(self, request):

        if authenticator(self.request):
            stack = CarStack.objects.order_by('input_in')
            return Response(stack, status=200)

        else:
            return Response(
                {
                    'msg': 'chave inválida'
                },
                status=401)
    def post(self, request):

        pass

