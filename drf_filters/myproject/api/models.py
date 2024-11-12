from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=100)
    roll = models.IntegerField()
    subject = models.CharField(max_length=100)
    checked_by = models.CharField(max_length=100)
    
