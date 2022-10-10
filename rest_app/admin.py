from django.contrib import admin
from .models import Student

class student_model(admin.ModelAdmin):
    pass
admin.site.register(Student, student_model)
