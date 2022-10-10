from rest_framework import serializers
from .models  import *

class student_serilizer(serializers.ModelSerializer):
    class Meta:
        model=Student
        #fields='__all__'
        #fields=['Naame','Age']
        exclude=['id']