from django.urls import path
from .views import *


"""
API endpoints for bookings
api/bookings/listuser/ - GET request (requires authentication)
    Required fields: None
    Returns: list of bookings for user
api/bookings/listhotel/ - GET request
    Required fields: hotel_id
    Returns: list of bookings for hotel
api/bookings/create/ - POST request (requires authentication)
    Required fields: room_id, checkin_date, checkout_date
    Returns: created booking
api/bookings/update/<booking_id>/ - PUT request (requires authentication)
    Required fields: None
    Optional fields: room_id, checkin_date, checkout_date
    Returns: updated booking
api/bookings/delete/<booking_id>/ - DELETE request (requires authentication)
    Required fields: None
    Returns: None
"""
urlpatterns = [
    path("listuser/", ListViewUser, name="listuser"),
    path("listhotel/", ListViewHotel, name="listhotel"),
    path("create/", CreateView, name="create"),
    path("update/<booking_id>/", UpdateView, name="update"),
    path("delete/<booking_id>/", DeleteView, name="delete"),
]
