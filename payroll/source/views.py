from django.shortcuts import render, HttpResponse


# Create your views here.
def index(request):
    return render(request, 'source/index.html', context={})


def addEmployee(request):
    # code for addEmployee
    pass


def deleteEmployee(request):
    # code for deleting an Employee
    pass


def viewEmployeeList(request):
    # code for deleting an Employee
    pass


def viewPaySlip(request):
    # code for deleting an Employee
    pass


def generatePaySlip(request):
    # code for deleting an Employee
    pass
