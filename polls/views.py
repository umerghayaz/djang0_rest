
# Create your views here.
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
@api_view(['GET'])
def index(request):
    return Response({'status':200,'message':'HELLO USER'})
