from django.urls import path, include
from . import views

app_name = 'trips'

urlpatterns = [
    path('list', views.list_trips, name='list_trips'),
    path('create', views.create_trip, name='create_trip'),
    path('<str:trip_id>', views.get_trip, name='get_trip'),
    path('delete/<str:trip_id>', views.delete_trip, name='delete_trip'),
    path('update/<str:trip_id>', views.update_trip, name='update_trip')
]