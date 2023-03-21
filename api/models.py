from django.db import models
from django.utils import timezone
# Create your models here.

class Employee(models.Model):
	name = models.CharField(max_length=255)
	age = models.IntegerField()
	gender = models.CharField(max_length=255,choices=(("M","Male"),("F","Female"),("T","Transgender")))
	department = models.CharField(max_length=255)
	salary = models.FloatField()
	is_active = models.BooleanField(default=True)
	created_by = models.IntegerField(default=1)
	created_on = models.DateTimeField(default=timezone.now)

	def __str__(self):
		return self.name

	class Meta:
		ordering = ['id']
