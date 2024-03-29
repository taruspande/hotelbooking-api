from .serializers import *
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken
import re

regex1 = re.compile(
    r"^(?:[A-Za-z0-9!#$%&'*+/=?^_`{|}~-]+\.)*[A-Za-z0-9!#$%&'*+/=?^_`{|}~-]+@(?!-)[a-zA-Z0-9-]{1,63}(?<!-)(?:\.(?!-)[a-zA-Z0-9-]{1,63}(?<!-))*$"
)
regex2 = re.compile(r"^[^@]{1,64}@[^@]{1,255}$")


# Create your views here.
@api_view(http_method_names=["POST"])
def RegisterView(request):
    try:
        username = request.data["username"]
        if not (re.fullmatch(regex1, username) and re.fullmatch(regex2, username)):
            return Response(status=status.HTTP_400_BAD_REQUEST)
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    except Exception:
        return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(http_method_names=["POST"])
def LogoutView(request):
    try:
        refresh_token = request.data["refresh"]
        token = RefreshToken(refresh_token)
        token.blacklist()
        return Response(status=status.HTTP_205_RESET_CONTENT)
    except Exception:
        return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(http_method_names=["GET"])
@permission_classes([IsAuthenticated])
def UserView(request):
    try:
        serializer = UserSerializer(request.user)
        data = {}
        for key in serializer.data:
            if key == "first_name" or key == "last_name" or key == "username":
                data[key] = serializer.data[key]
        return Response(data)
    except Exception:
        return Response(status=status.HTTP_400_BAD_REQUEST)
