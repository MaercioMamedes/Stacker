from django.contrib import admin
from core.models import Car


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    pass


