# -*- coding: utf-8 -*-
"""
Created on Mon Oct 10 14:03:26 2022

@author: Dell
"""

from django.contrib import admin
from django.urls import path,include
from rest_app import views
urlpatterns = [
    path("admin/", admin.site.urls),
    path("test/",views.hello_world),
    path("test1/",views.student_post)]