from django.db import models

# Create your models here.
class student(models.Model):
    stu_name=models.CharField(max_length=200)
    stu_no=models.CharField(max_length=100)
    stu_roll=models.IntegerField()
    def __str__(self) -> str:
        return f"{self.stu_name} {self.stu_roll}"

class Emp(models.Model):
    emp_name=models.CharField(max_length=255,null=True,blank=True)
    emp_id=models.IntegerField()
    emp_sal=models.FloatField()