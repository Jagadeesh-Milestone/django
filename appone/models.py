from django.db import models

class student(models.Model):
    firstname=models.CharField(max_length=20)
    lastname=models.CharField(max_length=20)
    course=models.CharField(max_length=10)
    joindate=models.DateField()
    contact=models.BigIntegerField()

