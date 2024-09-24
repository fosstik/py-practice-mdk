"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static 
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('practic1/', include('practic1.urls')),
    path('practic2/', include('practic2.urls')),
    path('practic6/', include('practic6.urls')),
    path('practic7/', include('practic7.urls')),
    path('practic8/', include('practic8.urls')),
    path('practic9/', include('practic9.urls')),
    path('practic10/', include('practic10.urls')),
    path('practic11/', include('practic11.urls')),
    path('practic12/', include('practic12.urls')),
    path('practic13/', include('practic13.urls')),
    path('practic14/', include('practic14.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)