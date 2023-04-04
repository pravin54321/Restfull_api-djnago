from django.contrib import admin
from .models import *

# Register your models here.
class Stu_Admin(admin.ModelAdmin):
    list_display=['id','stu_name','stu_no','stu_roll']
admin.site.register(student,Stu_Admin)   
class EmpAdmin(admin.ModelAdmin):
    pass
admin.site.register(Emp,EmpAdmin) 
