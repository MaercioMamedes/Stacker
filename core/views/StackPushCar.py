from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from core.serializer import CarSerializer
from core.helpers import authenticator, get_stack
from core.models import Car, CarStack


class StackPushCar(GenericAPIView):
    serializer_class = CarSerializer
    queryset = CarStack.objects.all().order_by('-input_in')

    def post(self, request):

        if authenticator(self.request):
            serializer = self.get_serializer(data=self.request.data)
            serializer.is_valid(raise_exception=True)

            """creating a car object"""
            if serializer.is_valid():
                car = Car.objects.create(
                    brand=serializer.validated_data['brand'],
                    model=serializer.validated_data['model'],
                    color=serializer.validated_data['color'],
                    license_plate=serializer.validated_data['license_plate']
                )

                """Adding car to stack"""
                push_car = CarStack.objects.create(car=car)

                return Response(get_stack(self.get_queryset()))

        else:
            return Response(
                {
                    'msg': 'chave inválida'
                }, status=401)
