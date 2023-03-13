from core.models import Car


def create_car(**car_data):
    car = Car.objects.create(
        brand=car_data['brand'],
        model=car_data['model'],
        color=car_data['color'],
        license_plate=car_data['license_plate']
    )

    return car
