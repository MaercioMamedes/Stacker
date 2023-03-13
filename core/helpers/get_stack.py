from django.utils import timezone
from datetime import datetime


def get_stack(stack):

    def format_date_time(input_in):
        date_time = timezone.localtime(input_in)
        return date_time.strftime('%d-%m-%Y %H:%M:%S')

    return list(
        map(
            lambda car_stack:
            {
                'marca': car_stack.car.brand,
                'modelo': car_stack.car.model,
                'cor': car_stack.car.color,
                'placa': car_stack.car.license_plate.upper(),
                'entrada no pátio': format_date_time(car_stack.input_in),
            },
            stack
        )
    )
