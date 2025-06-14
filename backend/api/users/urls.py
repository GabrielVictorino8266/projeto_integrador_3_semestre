from django.urls import path
from . import views # views
from .swagger.swagger_decorators import (
    login_swagger,
    refresh_token_swagger,
    user_profile_swagger,
    logout_swagger
)

app_name = 'users'
urlpatterns = [
    path('login/', login_swagger(views.login), name='login'),
    path('refresh-token/', refresh_token_swagger(views.refresh_token_view), name='refresh_token'),
    path('logout/', logout_swagger(views.logout), name='logout'),
    path('profile/', user_profile_swagger(views.get_user_profile), name='user_profile'),
]