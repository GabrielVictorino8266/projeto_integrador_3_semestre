from django.urls import path
from . import controller # views
from .swagger.swagger_decorators import (
    login_swagger,
    refresh_token_swagger,
    user_profile_swagger,
    logout_swagger
)

urlpatterns = [
    path('login/', login_swagger(controller.login), name='login'),
    path('refresh-token/', refresh_token_swagger(controller.refresh_token_view), name='refresh_token'),  # CORRIGIDO
    path('logout/', logout_swagger(controller.logout), name='logout'),
    path('profile/', user_profile_swagger(controller.get_user_profile), name='user_profile'),
]