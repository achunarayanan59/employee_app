from django.forms import ModelForm
from django import forms
from . models import Employee_data_base

class EmployeeForm(ModelForm):
    class Meta:
        model=Employee_data_base
        fields='__all__'
        widgets = {
            'firstname': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name'}),
            'lastname': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name'}),
            'empid': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Employee ID'}),
            'department': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Department'}),
            'salary': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Salary'}),
            'age': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Age'}),
        }