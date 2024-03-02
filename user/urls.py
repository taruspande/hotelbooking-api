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
    Required fields: username, password
    Optional fields: email, first_name, last_name
    Returns: None
api/user/details/ - GET request (requires authentication)
    Required fields: None
    Returns: user details
"""
urlpatterns = [
    path("login/", TokenObtainPairView.as_view(), name="login"),
    path("login/refresh/", TokenRefreshView.as_view(), name="login_refresh"),
    path("logout/", LogoutView, name="logout"),
    path("register/", RegisterView, name="register"),
    path("details/", UserView, name="details"),
]
