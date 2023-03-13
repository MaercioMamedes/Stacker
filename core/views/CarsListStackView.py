from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from core.models import CarStack
from core.models import Car
from core.serializer import CarSerializer
from core.helpers import authenticator, get_stack


class CarsListStackView(GenericAPIView):
    serializer_class = CarSerializer
    queryset = CarStack.objects.all().order_by('-input_in')

    def get(self, request):

        if authenticator(self.request):

            return Response(get_stack(self.get_queryset()))

        else:
            return Response(
                {
                    'msg': 'chave inválida'
                },
                status=401)
