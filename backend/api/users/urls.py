from django.urls import path
from . import controller

urlpatterns = [
    path('login/', controller.login, name='login'),
    path('refresh-token/', controller.refresh_token_view, name='refresh_token'),  # CORRIGIDO
    path('logout/', controller.logout, name='logout'),
    path('profile/', controller.get_user_profile, name='user_profile'),
]