from django.shortcuts import render, HttpResponse
from .models import Employee
from .forms import EmployeeForm


# Create your views here.
def index(request):
    # Shows employee list by default
    if request.method == 'GET':
        empList = Employee.objects.all()
    context = {'empList': empList}
    return render(request, 'source/index.html', context=context)


def add_employee(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            print("Form Data", form.cleaned_data)
            emp = Employee()
            emp.name = form.cleaned_data['name']
            emp.empid = form.cleaned_data['empid']
            emp.designation = form.cleaned_data['designation']
            emp.department = form.cleaned_data['department']
            emp.email = form.cleaned_data['email']
            emp.save()
            return HttpResponse("Employee Added")
    else:
        form = EmployeeForm()
        context = {'form': form}
        return render(request, 'source/add_emp_form.html', context=context)



def del_employee(request, id):
    emp = Employee.objects.get(empid=id)
    emp.delete()
    return HttpResponse("Employee Deleted")


def update_employee(request, id):
    emp = Employee.objects.get(empid=id)
    return HttpResponse("Employee updated")


def view_payslip(request, id):
    return HttpResponse("View Payslip")


def generate_payslip(request):
    return HttpResponse("Payslip Generated")
