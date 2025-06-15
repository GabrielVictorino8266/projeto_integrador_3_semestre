from django.urls import path
from . import views
from .swagger.users_swagger import (
    login_swagger,
    refresh_swagger,
    logout_swagger,
    profile_swagger
)

app_name = 'users'
urlpatterns = [
    path('login/', login_swagger(views.login), name='login'),
    path('refresh-token/', refresh_swagger(views.refresh), name='refresh_token'),
    path('logout/', logout_swagger(views.logout), name='logout'),
    path('profile/', profile_swagger(views.user_profile), name='user_profile'),
]