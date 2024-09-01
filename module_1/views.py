from django.shortcuts import render,redirect
from . models import Employee_data_base
from . forms import EmployeeForm
# Create your views here.
def index(request):
    return render(request,'index.html')

def add_employee(request):
    if request.POST:
        added_data=EmployeeForm(request.POST)
        if added_data.is_valid():
            added_data.save()
            return redirect('view_employee')
    else:
        emp_form=EmployeeForm()
    return render(request,'add_employee.html',{'emp_form':emp_form})

def view_employee(request):
    employee_list=Employee_data_base.objects.all()
    return render(request,'view_employee.html',{'employee_list':employee_list})

def view_edit_or_delete_emp(request):
    employee_list=Employee_data_base.objects.all()
    return render(request,'view_edit_or_delete_emp.html',{'employee_list':employee_list})

def delete_emp(request,pk):
    delete_instance=Employee_data_base.objects.get(pk=pk)
    delete_instance.delete()
    return redirect('view_edit_or_delete_emp')

def edit_emp(request,pk):
    edit_instance=Employee_data_base.objects.get(pk=pk)
    if request.POST:
        updated_emp_form=EmployeeForm(request.POST,instance=edit_instance)
        if updated_emp_form.is_valid():
            updated_emp_form.save()      
            return redirect('view_edit_or_delete_emp')
    else:
        emp_form=EmployeeForm(instance=edit_instance)
    return render(request,'edit.html',{'emp_form':emp_form})