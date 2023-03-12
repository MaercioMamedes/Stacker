from django.contrib import admin
from django.urls import path
from core.views import OrderView, CarsListStackView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', CarsListStackView.as_view(), name='index'),
]
