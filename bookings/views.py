from .serializers import *
from rooms.serializers import *
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated


# Create your views here.
@api_view(http_method_names=["GET"])
@permission_classes([IsAuthenticated])
def ListUserView(request):
    try:
        user_id = request.user.id
        bookings = Booking.objects.filter(user_id=user_id)
        serializer = BookingSerializer(bookings, many=True)
        return Response(serializer.data)
    except Exception:
        return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(http_method_names=["GET"])
def ListHotelView(request):
    try:
        hotel_id = request.query_params.get("hotel_id")
        rooms = Room.objects.filter(hotel_id=hotel_id)
        room_ids = [room.room_id for room in rooms]
        bookings = Booking.objects.filter(room_id__in=room_ids)
        serializer = BookingSerializer(bookings, many=True)
        return Response(serializer.data)
    except Exception:
        return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(http_method_names=["POST"])
@permission_classes([IsAuthenticated])
def CreateView(request):
    try:
        user_id = request.user.id
        data = request.data
        data["user_id"] = user_id
        serializer = BookingSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    except Exception:
        return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(http_method_names=["PUT"])
@permission_classes([IsAuthenticated])
def UpdateView(request, booking_id):
    try:
        room_id = request.data.get("room_id")
        checkin_date = request.data.get("checkin_date")
        checkout_date = request.data.get("checkout_date")
        booking = Booking.objects.get(booking_id=booking_id)
        data = {
            "booking_id": booking_id,
            "room_id": room_id if room_id else str(booking.room_id),
            "checkin_date": checkin_date if checkin_date else booking.checkin_date,
            "checkout_date": checkout_date if checkout_date else booking.checkout_date,
        }
        serializer = BookingSerializer(booking, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    except Booking.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    except Exception:
        return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(http_method_names=["DELETE"])
@permission_classes([IsAuthenticated])
def DeleteView(request, booking_id):
    try:
        booking = Booking.objects.get(booking_id=booking_id)
        booking.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    except Booking.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    except Exception:
        return Response(status=status.HTTP_400_BAD_REQUEST)
