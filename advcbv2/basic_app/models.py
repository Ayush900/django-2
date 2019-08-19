from django.db import models

# Create your models here.

class School(models.Model):
    name = models.CharField(max_length = 264)
    principal = models.CharField(max_length = 264)
    location = models.CharField(max_length = 264)

class Student(models.Model):
    name = models.CharField(max_length = 264)
    age = models.PositiveIntegerField()
    school = models.ForeignKey(School,related_name='students',on_delete=models.CASCADE)
