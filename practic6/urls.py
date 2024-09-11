from django.urls import path
from practic6.views import get_info, get_author 

urlpatterns = [
    path('main/', get_info),
    path('authors/', get_author),
]