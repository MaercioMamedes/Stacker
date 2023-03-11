from rest_framework.generics import ListAPIView
from core.models import CarStack


class CarsListStackView(ListAPIView):

    def get_queryset(self):

        return CarStack.objects.order_by("input_in")