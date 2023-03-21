from django.shortcuts import render
from .serializers import EmployeeSerializers
from rest_framework.views import APIView
from .models import Employee
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate,logout
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import AllowAny
from rest_framework import renderers
import json
from rest_framework.pagination import PageNumberPagination
# Create your views here.

class UserRenderer(renderers.JSONRenderer):
	charset='utf-8'
	def render(self, data, accepted_media_type=None, renderer_context=None):
		response = ''
		if 'ErrorDetail' in str(data):
			response = json.dumps({'errors':data})
		else:
			response = json.dumps(data)

		return response

def get_tokens_for_user(user):
  refresh = RefreshToken.for_user(user)
  return {
      'refresh': str(refresh),
      'access': str(refresh.access_token),
  }

class UserLoginView(APIView):
	renderer_classes = [UserRenderer]
	permission_classes = (AllowAny,)
	def post(self, request, format=None):
		username = request.data.get('username')
		password = request.data.get('password')
		user = authenticate(username=username, password=password)
		if user is not None:
			token = get_tokens_for_user(user)
			return Response({'token':token, 'msg':'Login Success'}, status=status.HTTP_200_OK)
		else:
			return Response({'message':'Username or Password is not Valid'}, status=status.HTTP_404_NOT_FOUND)

class EmployeeView(APIView):
	renderer_classes = [UserRenderer]
	permission_classes = (IsAuthenticated,)
	def post(self,request,*args,**kwargs):
		employee_serializers = EmployeeSerializers(data=request.data)
		if employee_serializers.is_valid():
			employee_serializers.save()
			return Response(employee_serializers.data, status=status.HTTP_201_CREATED)
		return Response(employee_serializers.errors, status=status.HTTP_400_BAD_REQUEST)

	def get_object(self, id):
	    try:
	        return Employee.objects.get(id=id)
	    except Employee.DoesNotExist:
	        return None

	def get(self,request,id,*args,**kwargs):
		employee = self.get_object(id)
		if not employee:
			return Response({"message": "Employee id does not exists"}, status=status.HTTP_400_BAD_REQUEST)
		employee_serializers = EmployeeSerializers(employee,many=True)
		return Response(employee_serializers.data, status=status.HTTP_200_OK)

	def put(self,request,id,*args,**kwargs):
		employee = self.get_object(id)
		if not employee:
			return Response({"message": "Employee id does not exists"}, status=status.HTTP_400_BAD_REQUEST)
		employee_serializers = EmployeeSerializers(employee,data=request.data)
		if employee_serializers.is_valid():
			employee_serializers.save()
			return Response(employee_serializers.data, status=status.HTTP_201_CREATED)
		return Response(employee_serializers.errors, status=status.HTTP_400_BAD_REQUEST)

	def delete(self,request,id,*args,**kwargs):
		employee = self.get_object(id)
		if not employee:
			return Response({"message": "Employee id does not exists"}, status=status.HTTP_400_BAD_REQUEST)
		employee.delete()
		return Response({"message": "Employee Deleted Successfully"}, status=status.HTTP_200_OK)

class AllEmployee(APIView):
	renderer_classes = [UserRenderer]
	permission_classes = (IsAuthenticated,)

	def get(self,request,*args,**kwargs):
		employee = Employee.objects.all()
		paginator = PageNumberPagination()
		paginator.page_size = 2
		result_page = paginator.paginate_queryset(employee, request)
		serializer = EmployeeSerializers(result_page, many=True)
		return paginator.get_paginated_response(serializer.data)