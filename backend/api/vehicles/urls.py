from django.urls import path
from . import views
from .swagger.vehicle_swagger import (
    create_vehicle_swagger,
    update_vehicle_swagger,
    delete_vehicle_swagger,
    list_vehicles_swagger,
    get_vehicle_swagger,
    list_vehicle_status_swagger
)

app_name = 'vehicles'
urlpatterns = [
    path('create/', create_vehicle_swagger(views.create_vehicle), name='create_vehicle'),
    path('update/<str:id>/', update_vehicle_swagger(views.update_vehicle), name='update_vehicle'),
    path('delete/<str:id>/', delete_vehicle_swagger(views.delete_vehicle), name='delete_vehicle'),
    path('status/', list_vehicle_status_swagger(views.list_vehicle_status), name='list_vehicle_status'),
    path('<str:id>/', get_vehicle_swagger(views.get_vehicle), name='get_vehicle'),
    path('', list_vehicles_swagger(views.list_vehicles), name='list_vehicles'),
]