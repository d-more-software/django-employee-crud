from django.shortcuts import render , redirect , get_object_or_404
from .models import Employee
from .forms import EmployeeForm

def employees_list(request):
    employees = Employee.objects.all()
    return render (request, "employee/list.html", {'employees':employees})


def add_employee(request):
    form = EmployeeForm(request.POST or None)
    if form.is_valid():
        form.save() 
        return redirect('employees_list')
    return render (request, "employee/form.html", {'form':form})

def update_employee(request,id):
    employee = get_object_or_404(Employee, id=id)
    form = EmployeeForm(request.POST or None,instance=employee)
    if form.is_valid():
        form.save() 
        return redirect('employees_list')
    return render (request, "employee/form.html", {'form':form})

def delte_employee(request,id):
    employee = get_object_or_404(Employee, id=id)
    if request.method == 'POST':
        employee.delete()
        return redirect('employees_list')
    return render (request, "employee/delete_employee.html", {'employee':employee})



