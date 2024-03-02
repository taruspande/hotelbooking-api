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
