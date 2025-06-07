from django.urls import path, include
from . import views

app_name = 'drivers'

urlpatterns = [
    path('list', views.list_drivers, name='list_drivers'),
]