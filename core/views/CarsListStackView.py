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

    def post(self, request):

        if authenticator(self.request):
            serializer = self.get_serializer(data=self.request.data)
            serializer.is_valid(raise_exception=True)
            if serializer.is_valid():
                car = Car.objects.create(
                    brand=serializer.validated_data['brand'],
                    model=serializer.validated_data['model'],
                    color=serializer.validated_data['color'],
                    license_plate=serializer.validated_data['license_plate']
                )

                push_car = CarStack.objects.create(car=car)

                stack = list(CarStack.objects.order_by('input_in'))
                print('passou aqui')
                return Response(stack, status=200)

        else:
            return Response(
                {
                    'msg': 'chave inválida'
                }, status=401)
