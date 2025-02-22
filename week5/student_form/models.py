# student_app/models.py

from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=100)
    dob = models.DateField()
    address = models.TextField()
    contact = models.CharField(max_length=15)
    email = models.EmailField()
    english_marks = models.IntegerField()
    physics_marks = models.IntegerField()
    chemistry_marks = models.IntegerField()

    def __str__(self):
        return self.name
