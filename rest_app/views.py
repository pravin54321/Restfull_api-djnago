from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import *
from .serilizer import *


@api_view()
def hello_world(request):
    student_info=Student.objects.all()

    serilizer=student_serilizer(student_info,many=True)
    return Response({"status":200,"pyload": serilizer.data})
@api_view(["POST"])
def student_post(request): #take data from front_end
    data=request.data
    print(data)
    serilizer=student_serilizer(data=request.data)
    if not serilizer.is_valid():
        return Response({"status":403, "message":"Something Wrong"})
    serilizer.save()
    return Response({"status":200, "pyload":data,"message":"msg send"})