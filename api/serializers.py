from rest_framework import serializers
from .models import Employee
from django.contrib.auth.models import User

class EmployeeSerializers(serializers.ModelSerializer):
	class Meta:
		model = Employee
		fields = "__all__"

	def validate(self,data):
		age = data.get('age')
		if age >= 60:
			raise serializers.ValidationError("Age must be below 60")
		gender = data.get('gender')
		if not gender:
			raise serializers.ValidationError("Gender not valid")
		return data