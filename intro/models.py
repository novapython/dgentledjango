from django.db import models

# Create your models here.

class Teacher(models.Model):

    name = models.CharField(max_length=64)
    favorite_number = models.IntegerField()

class Student(models.Model):

    name = models.CharField(max_length=64)
    goal = models.CharField(max_length=128)
