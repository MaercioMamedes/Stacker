from django.db import models
from core.models import Car


class CarStack(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    input_in = models.DateTimeField('entrada', auto_now=True)

