from .models import *
from rest_framework import serializers

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model= student
        fields="__all__"
class EmpSerializer(serializers.Serializer):
     emp_name=serializers.CharField(max_length=255)
     emp_id=serializers.IntegerField()
     emp_sal=serializers.FloatField()        
    