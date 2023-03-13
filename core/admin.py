from django.contrib import admin
from core.models import Car, CarStack


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    pass


@admin.register(CarStack)
class CarStackAdmin(admin.ModelAdmin):
    pass


