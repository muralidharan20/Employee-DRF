from django.test import TestCase
from .models import Employee

# Create your tests here.
class ModelsTestCase(TestCase):
	def test_employee_create(self):
		employee = Employee.objects.create(name="Murali",age=25,gender="M",salary=20000,department="IT")
		self.assertEqual(employee.name, 'Murali')
		self.assertEqual(employee.age, 25)
		self.assertEqual(employee.gender, "M")
		self.assertEqual(employee.salary, 20000)
		self.assertEqual(employee.department, "IT")

class ViewsTestCase(TestCase):
    def test_all_employee(self):
        employee_response = self.client.get('127.0.0.1:8000')
        self.assertEqual(employee_response.status_code, 404)