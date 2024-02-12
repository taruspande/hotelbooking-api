from rest_framework.decorators import api_view
from .models import *
from rest_framework.response import Response
from rest_framework import status

# Create your views here.


@api_view(http_method_names=["POST"])
def LoginView(Request):
    pass


@api_view(http_method_names=["POST"])
def RegisterView(Request):
    pass
