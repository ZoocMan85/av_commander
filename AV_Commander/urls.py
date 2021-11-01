"""AV_Commander URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.views.generic.base import TemplateView
from django.urls import path, include
from AV_Central import views as AV_Central_views
import AV_Central
from api import views as API_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', AV_Central_views.home_page,name = 'home'),
    path('home/', AV_Central_views.home_page,name = 'home'),
    path('api/power_on', API_views.power_on,name = 'power_on'),
    path('api/power_off', API_views.power_off,name = 'power_off'),
    path('api/volume_down', API_views.volume_down,name = 'volume_down'),
    path('api/volume_up', API_views.volume_up,name = 'volume_up'),
]
