from django.contrib import admin
from django.urls import path
from core.views import CarsListStackView, StackPushCar, StackPopCar

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', CarsListStackView.as_view(), name='index'),
    path('inserir-carro/', StackPushCar.as_view(), name='push_car'),
    path('remover-carro/', StackPopCar.as_view(), name='pop_car'),
]
