from django.urls import path
from .views import *


"""
API endpoints for rooms
api/rooms/list/ - GET request
    Optional fields: hotel_id
    Returns: list of rooms
"""
urlpatterns = [
    path("list/", ListView, name="list"),
    path("create/", CreateView, name="create"),
]
