from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
import json
import datetime
from django.views.decorators.csrf import csrf_exempt, csrf_protect
from django.views.generic import View
from .models import *
from rest_framework import serializers
from django.core.serializers import serialize
from .mixin import *
#from django import serialize

@csrf_exempt
def api_test(request):
    emp_data={'emp_name':'pravin mendhe','emp_sal':15000,'emp_no':9404300883}
    rep='<h1> emp_name:{} <br> emp_sal:{} <br> emp_no:{} </h1>'.format(emp_data['emp_name'],emp_data['emp_sal'],emp_data['emp_no'])
    json_data=json.dumps(rep)
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    return JsonResponse(emp_data)

class jsonCBV(View):
    def get(self,*args, **kwargs):
        emp_data={'Emp_Name':'pravin',"Emp_Sal":15000,"Emp_No":101}
        return JsonResponse(emp_data)        
def sum(*args):
    total=0
    for x in args:
        total=total+x
    print(total)
      
def sum_test(request):
    sum()
    sum(10,20,30)
    sum(10,20,30,40)
    sum(10,20,30,40,50) 
    return HttpResponse('ok')   
         
 ###################Serialization##########################  

class Test(View):
    def get(self,request,*args, **kwargs):
        emp_data=student.objects.get(id=1)
        final_list=[]
        #json_data=serialize('json',[emp_data],fields=('stu_name','stu_no'))
        json_data=self.serialize([emp_data])
        pdict=json.loads(json_data)
        for obj  in pdict:
            final_list.append(obj['fields'])
        print(final_list)
        return HttpResponse(json_data,content_type='application/json')
#############################################################################
class StudentList(SerializerMixin,View):
    def get(self,request,*args, **kwargs):
        qs=student.objects.all()
        json_data=self.serialize(qs)
        return HttpResponse(json_data,content_type='application/json')
    
########################################################################
class jsonCBV(Json_Response_Mixin,View):
    def get(self,request,*args, **kwargs):
        emp_data={"emp_name":"pravin","emp_sal":10000,"emp_id":102}  
        return self.render_to_json_response(emp_data)  
        
