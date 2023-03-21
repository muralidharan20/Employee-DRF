from django.urls import path
from .views import *
from rest_framework_swagger.views import get_swagger_view

schema_view = get_swagger_view(title='Employee DRF API')

urlpatterns = [
	path('login/',UserLoginView.as_view()),
	path('employee/',EmployeeView.as_view()),
	path('employee/<int:id>/',EmployeeView.as_view()),
	path('all_employee/',AllEmployee.as_view()),
	path('employee_documentation/',schema_view)
]