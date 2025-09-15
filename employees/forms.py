from django import forms
from .models import Employee

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['username','email','job_title', 'salary']
        widgets = {
            'username' : forms.TextInput(attrs={
                'class': 'input w-full',
                'placeholder' : 'Your full name '
            }),
            'email' : forms.TextInput(attrs={
                'class': 'input w-full',
                'placeholder' : 'Your mail '
            }),
            'job_title' : forms.TextInput(attrs={
                'class': 'input w-full',
                'placeholder' : 'Your job title '
            }),
            'salary' : forms.TextInput(attrs={
                'class': 'input w-full',
                'placeholder' : 'Your salary '
            }),
        }
