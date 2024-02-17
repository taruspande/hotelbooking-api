from django.urls import path
from .views import *
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

"""
API endpoints for user authentication
api/user/login/ - POST request
    Required fields: username, password
    Returns: access, refresh
api/user/login/refresh/ - POST request
    Required fields: refresh
    Returns: access, access
api/user/logout/ - POST request
    Required fields: refresh
    Returns: None
api/user/register/ - POST request
    Required fields: username, first_name, last_name, email, password
    Returns: None
"""
urlpatterns = [
    path("login/", TokenObtainPairView.as_view(), name="login"),
    path("login/refresh/", TokenRefreshView.as_view(), name="login_refresh"),
    path("logout/", LogoutView, name="logout"),
    path("register/", RegisterView, name="register"),
    path("details/", UserView, name="details"),
]
