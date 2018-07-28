from django.shortcuts import render, HttpResponse
from .models import Employee
from .forms import EmployeeForm


# Create your views here.
def index(request):
    if request.method == 'GET':
        empList = Employee.objects.all()
    context = {'empList': empList}
    return render(request, 'source/index.html', context=context)


def add_employee(request):
    form = EmployeeForm()
    context = {'form': form}
    return render(request, 'source/add_emp_form.html', context=context)


def del_employee(request, id):
    return HttpResponse("Employee Deleted")


def view_employee_list(request):
    return HttpResponse("Employee List")


def view_payslip(request, id):
    return HttpResponse("View Payslip")


def generate_payslip(request):
    return HttpResponse("Payslip Generated")
