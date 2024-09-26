from django.urls import path
from .views import create_order

urlpatterns = [
    path('order/create', create_order, name='create_order'),
    ]