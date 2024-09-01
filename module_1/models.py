from django.db import models

class Employee_data_base(models.Model):
    firstname=models.CharField(max_length=250)
    lastname=models.CharField(max_length=250)
    empid=models.IntegerField()
    department=models.CharField(max_length=250)
    salary=models.IntegerField()
    age=models.IntegerField()