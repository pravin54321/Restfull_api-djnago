from django.db import models

class Student(models.Model):
    Naame=models.CharField(max_length=50)
    Age=models.IntegerField(default=18)
    Father_name=models.CharField(max_length=50)
