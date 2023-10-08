from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from config import views

urlpatterns = [
    path('', views.configuracion, name='configuracion')
]

