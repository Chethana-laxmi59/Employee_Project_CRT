from http import HTTPStatus

from django.shortcuts import render
import json
# Create your views here.
from django.http import HttpResponse,JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Student

@csrf_exempt
def add_employee(request):
    if request.method == "POST":
        data=json.loads(request.body)
        emp_data = Student.objects.create(
            id=data.get('id'),
            name=data.get('name'),
            email=data.get('email'),
            phone=data.get('phone'),
            address=data.get('address'),
            designation=data.get('designation'),
            emp_type=data.get('emp_type'),
            salary=data.get('salary'),
        )
        return HttpResponse({
            "data":emp_data.id ,
            "status":HTTPStatus.OK
        })

def get_employee_details(request):
    emp_data=Student.objects.all().values()
    response_data=list(emp_data)
    return JsonResponse({
        "data":response_data,
        "status":HTTPStatus.OK
    })
