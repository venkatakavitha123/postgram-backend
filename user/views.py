from django.shortcuts import render
from rest_framework.decorators import api_view
from .models import User
from .userSerializer import UserSerializer
from rest_framework import response

# Create your views here.
@api_view(['POST'])
def login(request):
    serializerData=UserSerializer(request.data)
    realUserData=serializerData.data
    print(realUserData)
    return response.Response
# Create your views here.
