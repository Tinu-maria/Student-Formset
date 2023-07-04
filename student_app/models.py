from django.db import models


# Create your models here.

class Student(models.Model):
    name = models.CharField(max_length=100)
    is_active = models.BooleanField(default=False)
    
    def __str__(self):
        return self.name
    
    
class Teacher(models.Model):
    students = models.ForeignKey(Student, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
    