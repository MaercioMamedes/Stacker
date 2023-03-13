from django.contrib import admin
from django.urls import path
from core.views import CarsListStackView, StackPushCar

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', CarsListStackView.as_view(), name='index'),
    path('inserir-carro/', StackPushCar.as_view(), name='push_car'),
]
