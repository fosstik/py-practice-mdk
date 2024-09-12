from django.urls import path
from practic7.views import main ,about,products

urlpatterns = [
    path('main/', main),
    path('about/', about),
    path('products/', products),
]