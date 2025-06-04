from django.urls import path
from . import views

urlpatterns = [
    path('', views.list_vehicles, name='list_vehicles'),
    path('<int:id>/', views.get_vehicle, name='get_vehicle'),
    path('create/', views.create_vehicle, name='create_vehicle'),
    path('update/<int:id>/', views.update_vehicle, name='update_vehicle'),
    path('delete/<int:id>/', views.delete_vehicle, name='delete_vehicle'),
]