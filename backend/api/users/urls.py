from django.urls import path
from . import controller

urlpatterns = [
    path('login/', controller.login, name='login'),
    path('refresh-token/', controller.refresh_token, name='refresh_token'),
    path('profile/', controller.get_user_profile, name='user_profile'),
]