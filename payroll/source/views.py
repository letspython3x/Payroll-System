from django.shortcuts import render, HttpResponse
from .models import Employee


# Create your views here.
def index(request):
    if request.method == 'GET':
        empList = Employee.objects.all()
    context = {'empList': empList}
    return render(request, 'source/index.html', context=context)


def add_employee(request):
    return HttpResponse("Employee Added")


def del_employee(request, id):
    return HttpResponse("Employee Deleted")


def view_employee_list(request):
    return HttpResponse("Employee List")


def view_payslip(request, id):
    return HttpResponse("View Payslip")


def generate_payslip(request):
    return HttpResponse("Payslip Generated")
