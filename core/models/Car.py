from django.db import models


class Car(models.Model):
    brand = models.CharField('Marca', max_length=20)
    model = models.CharField('Modelo', max_length=20)
    color = models.CharField('Cor', max_length=20)
    license_plate = models.CharField('Placa', max_length=8, unique=True)

    def __str__(self):
        return f'{self.brand} {self.model} {self.color} placa {self.license_plate}'

