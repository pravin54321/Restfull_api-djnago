from django.test import TestCase
import requests
BASE_URl='http://127.0.0.1'
ENDPOINT='api/'
r=requests.get(BASE_URl+ENDPOINT)
data=r.json()
print("emp_name==>",data['emp_name'])
print('emp_sal==>',data['emp_sal'])
print('emp_no==>',data['emp_no'])