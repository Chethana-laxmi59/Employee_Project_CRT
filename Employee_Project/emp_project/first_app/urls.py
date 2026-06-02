
from django.urls import path
from django.views.generic import detail

from .views import add_employee,get_employee_details

# http://127.0.0.1:8000/first/add_emp
# http://127.0.0.1:8000/first/get_data



urlpatterns = [
    path('add_emp', add_employee),
    path("get_data", get_employee_details),
]
