from django.urls import path, include
from . import views
from .swagger.driver_swagger import (
    list_drivers_swagger,
    create_driver_swagger,
    get_driver_swagger,
    update_driver_swagger,
    delete_driver_swagger
)

app_name = 'drivers'

urlpatterns = [
    path('list', list_drivers_swagger(views.list_drivers), name='list_drivers'),
    path('create', create_driver_swagger(views.create_driver), name='create_driver'),
    path('<str:driver_id>', get_driver_swagger(views.get_driver), name='get_driver'),
    path('delete/<str:driver_id>', delete_driver_swagger(views.delete_driver), name='delete_driver'),
    path('update/<str:driver_id>', update_driver_swagger(views.update_driver), name='update_driver')
]