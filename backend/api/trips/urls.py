from django.urls import path, include
from . import views
from .swagger.trip_swagger import create_trip_swagger, update_trip_swagger

app_name = 'trips'

urlpatterns = [
    path('list', views.list_trips, name='list_trips'),
    path('list/<str:trip_id>', views.get_trip, name='get_trip'),
    path('delete/<str:trip_id>', views.delete_trip, name='delete_trip'),
    path('create', create_trip_swagger(views.create_trip), name='create_trip'),
    path('update/<str:trip_id>', update_trip_swagger(views.update_trip), name='update_trip'),
]