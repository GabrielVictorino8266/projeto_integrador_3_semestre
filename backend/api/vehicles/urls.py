from django.urls import path
from . import controller

urlpatterns = [
    path('vehicles/', controller.list_vehicles, name='list_vehicles'),
    path('vehicles/<int:id>/', controller.get_vehicle, name='get_vehicle'),
    path('vehicles/create/', controller.create_vehicle, name='create_vehicle'),
    path('vehicles/update/<int:id>/', controller.update_vehicle, name='update_vehicle'),
    path('vehicles/delete/<int:id>/', controller.delete_vehicle, name='delete_vehicle'),
]