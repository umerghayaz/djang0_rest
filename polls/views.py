
# Create your views here.
from django.shortcuts import render
from django.views import View
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import *
from .serializers import *
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.tokens import RefreshToken

class RegisterAPI(APIView):

    def post(self,request):
        # data = request.data
        serializer = UserSerializer(data=request.data)
        if not serializer.is_valid():
            return Response({'status': 403, 'error': serializer.errors})
        serializer.save()
        user=User.objects.get(username=serializer.data['username'])
        refresh=RefreshToken.for_user(user=user)
        return Response({'status': 200, 'payload': serializer.data,'refresh': str(refresh),
        'access': str(refresh.access_token),})
class StudentAPI(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    def get(self,request):
        student_obj = Student.objects.all()
        serializer = StudentSerializer(student_obj, many=True)
        return Response({'status': 200, 'payload': serializer.data})

    def post(self,request):
        # data = request.data
        serializer = StudentSerializer(data=request.data)
        if not serializer.is_valid():
            return Response({'status': 403, 'error': serializer.errors})
        serializer.save()
        return Response({'status': 200, 'payload': serializer.data})
    def delete(self,request, id=None):
        try:
            # id=request.GET('id')
            student_obj = Student.objects.get(id=id)
            serializer=StudentSerializer( student_obj,data=request.data)
            student_obj.delete()
            return Response({'status':200,'message':'data deleted'})
        except Exception as e:
            return Response({'status':403,'message':'invalid id'})
    def patch(self,request):
        try:
            student_obj = Student.objects.get(id=request.data['id'])
            serializer=StudentSerializer( student_obj,data=request.data)
            if not serializer.is_valid():
                return Response({'status': 403, 'error': serializer.errors})
            serializer.save()
            return Response({'status':200,'payload':serializer.data})
        except Exception as e:
            return Response({'status':403,'message':'invalid id'})
#
# @api_view(['GET'])
# def index(request):
#     student_obj=Student.objects.all()
#     serializer=StudentSerializer(student_obj,many=True)
#     return Response({'status':200,'payload':serializer.data})
# @api_view(['POST'])
# def save_data(request):
#     data=request.data
#     serializer=StudentSerializer( data=request.data)
#     if not serializer.is_valid():
#         return Response({'status': 403, 'error': serializer.errors})
#     serializer.save()
#     return Response({'status':200,'payload':serializer.data})
# @api_view(['PUT'])
# def update_data(request,id):
#     try:
#         student_obj = Student.objects.get(id=id)
#         data=request.data
#         serializer=StudentSerializer( student_obj,data=request.data)
#         if not serializer.is_valid():
#             return Response({'status': 403, 'error': serializer.errors})
#         serializer.save()
#         return Response({'status':200,'payload':serializer.data})
#     except Exception as e:
#         return Response({'status':403,'message':'invalid id'})
# @api_view(['DELETE'])
# def delete_data(request,id):
#     try:
#         student_obj = Student.objects.get(id=id)
#         student_obj.delete()
#         return Response({'status':200,'message':'data deleted'})
#     except Exception as e:
#         return Response({'status':403,'message':'invalid id'})