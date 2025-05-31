from django.urls import path
from . import controller

urlpatterns = [
    path('', controller.list_vehicles, name='list_vehicles'),
    path('<int:id>/', controller.get_vehicle, name='get_vehicle'),
    path('create/', controller.create_vehicle, name='create_vehicle'),
    path('update/<int:id>/', controller.update_vehicle, name='update_vehicle'),
    path('delete/<int:id>/', controller.delete_vehicle, name='delete_vehicle'),
]