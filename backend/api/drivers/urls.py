from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register('drivers', views.DriverViewSet, basename='driver')

urlpatterns = [
    path('', include(router.urls)),
    path('drivers/', views.DashbiardView.as_view(), name='dashboard'),
]