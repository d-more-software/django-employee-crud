from django.contrib import admin
from django.urls import path 
from . import views

urlpatterns = [
    path('', views.employees_list, name='employees_list'),
    path('add_employee/', views.add_employee, name='employees_add'),
    path('update_employee/<int:id>', views.update_employee, name='employee_update'),
    path('delete_employee/<int:id>', views.delte_employee, name='employee_delete'),
]