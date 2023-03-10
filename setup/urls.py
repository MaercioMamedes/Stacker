from django.contrib import admin
from django.urls import path
from core.views import OrderView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', OrderView.as_view(), name='order'),
]
