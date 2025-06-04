from django.urls import path
from . import views

app_name = 'vehicles'
urlpatterns = [
    path('create/', views.create_vehicle, name='create_vehicle'),
    path('update/<str:id>/', views.update_vehicle, name='update_vehicle'),
    path('delete/<str:id>/', views.delete_vehicle, name='delete_vehicle'),
    path('<str:id>/', views.get_vehicle, name='get_vehicle'),
    path('', views.list_vehicles, name='list_vehicles'),
]