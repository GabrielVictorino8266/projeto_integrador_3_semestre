from django.urls import path
from . import views

app_name = 'users'
urlpatterns = [
    path('login/', views.login, name='login'),
    path('refresh-token/', views.refresh, name='refresh_token'),
    path('logout/', views.logout, name='logout'),
    path('profile/', views.user_profile, name='user_profile'),
]