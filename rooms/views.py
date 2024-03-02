from .serializers import *
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view


# Create your views here.
@api_view(http_method_names=["GET"])
def ListView(request):
    try:
        hotel_id = request.query_params.get("hotel_id")
        if hotel_id:
            rooms = Room.objects.filter(hotel_id=hotel_id)
        else:
            rooms = Room.objects.all()
        serializer = RoomSerializer(rooms, many=True)
        return Response(serializer.data)
    except Exception as e:
        return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(http_method_names=["POST"])
def CreateView(request):
    try:
        serializer = RoomSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(http_method_names=["PUT"])
def UpdateView(request, room_id):
    try:
        hotel_id = request.data.get("hotel_id")
        room_type = request.data.get("room_type")
        price_per_night = request.data.get("price_per_night")
        room_number = request.data.get("room_number")
        room = Room.objects.get(room_id=room_id)
        data = {
            "room_id": room_id,
            "hotel_id": hotel_id if hotel_id else str(room.hotel_id),
            "room_type": room_type if room_type else str(room.room_type),
            "price_per_night": (
                price_per_night if price_per_night else str(room.price_per_night)
            ),
            "room_number": room_number if room_number else str(room.room_number),
        }
        serializer = RoomSerializer(room, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(http_method_names=["DELETE"])
def DeleteView(request, room_id):
    try:
        room = Room.objects.get(room_id=room_id)
        room.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    except Exception as e:
        return Response(status=status.HTTP_400_BAD_REQUEST)
