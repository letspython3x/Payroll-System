"""payroll URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path(r'', views.index, name='index'),
    path(r'add/', views.add_employee, name='add_employee'),
    path(r'del/<str:id>', views.del_employee, name='del_employee'),
    path(r'update/<str:id>', views.update_employee, name='update_employee'),
    path(r'view/<str:id>', views.view_employee, name='view_employee'),
    path(r'payslip/<str:id>', views.view_payslip, name='view_payslip'),
    path(r'generate_payslip/', views.generate_payslip, name='generate_payslip'),

]
