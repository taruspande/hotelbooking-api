from django.urls import path
from .views import *


"""
API endpoints for rooms
api/rooms/list/ - GET request
    Optional fields: hotel_id
    Returns: list of rooms
api/rooms/create/ - POST request
    Required fields: hotel_id, room_type, price_per_night, room_number
    Returns: created room
api/rooms/update/ - PUT request
    Required fields: room_id
    Optional fields: hotel_id, room_type, price_per_night, room_number
    Returns: updated room
"""
urlpatterns = [
    path("list/", ListView, name="list"),
    path("create/", CreateView, name="create"),
    path("update/", UpdateView, name="update"),
]
