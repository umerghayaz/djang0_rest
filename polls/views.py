
# Create your views here.
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import *
from .serializers import *
@api_view(['GET'])
def index(request):
    student_obj=Student.objects.all()
    serializer=StudentSerializer(student_obj,many=True)
    return Response({'status':200,'payload':serializer.data})
@api_view(['POST'])
def save_data(request):
    data=request.data
    serializer=StudentSerializer( data=request.data)
    if not serializer.is_valid():
        return Response({'status': 403, 'error': serializer.errors})
    serializer.save()
    return Response({'status':200,'payload':serializer.data})
@api_view(['PUT'])
def update_data(request,id):
    try:
        student_obj = Student.objects.get(id=id)
        data=request.data
        serializer=StudentSerializer( student_obj,data=request.data)
        if not serializer.is_valid():
            return Response({'status': 403, 'error': serializer.errors})
        serializer.save()
        return Response({'status':200,'payload':serializer.data})
    except Exception as e:
        return Response({'status':403,'message':'invalid id'})
@api_view(['DELETE'])
def delete_data(request,id):
    try:
        student_obj = Student.objects.get(id=id)
        student_obj.delete()
        return Response({'status':200,'message':'data deleted'})
    except Exception as e:
        return Response({'status':403,'message':'invalid id'})