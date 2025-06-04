from django.urls import path
from . import views

urlpatterns = [
    path('', views.list_vehicles, name='list_vehicles'),
    path('<str:id>/', views.get_vehicle, name='get_vehicle'),
    path('create/', views.create_vehicle, name='create_vehicle'),
    path('update/<str:id>/', views.update_vehicle, name='update_vehicle'),
    path('delete/<str:id>/', views.delete_vehicle, name='delete_vehicle'),
]