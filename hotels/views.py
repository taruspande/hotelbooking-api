from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Hotel
from .serializers import HotelSerializer

@api_view(['GET'])
def hotel_list(request):
    try:
        hotels = Hotel.objects.all()
        serializer = HotelSerializer(hotels, many=True)
        return Response(serializer.data)
    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def create_hotel(request):
    try:
        serializer = HotelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
def update_hotel(request, hotel_id):
    try:
        hotel = Hotel.objects.get(hotel_id=hotel_id)
        serializer = HotelSerializer(hotel, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    except Hotel.DoesNotExist:
        return Response({"error": "Hotel not found"}, status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def delete_hotel(request, hotel_id):
    try:
        hotel = Hotel.objects.get(hotel_id=hotel_id)
        hotel.delete()
        return Response({"message": "Hotel deleted successfully"}, status=status.HTTP_204_NO_CONTENT)
    except Hotel.DoesNotExist:
        return Response({"error": "Hotel not found"}, status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
