from django.urls import path, include
from . import views

urlpatterns = [
    path('list', views.list_drivers, name='list_drivers'),
]