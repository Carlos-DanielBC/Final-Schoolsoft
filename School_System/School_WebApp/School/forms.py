from django import forms
from .models import *

class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['level']
        widgets = {
            'level': forms.TextInput(attrs={'class': 'form-control'})
        }

class SubjectForm(forms.ModelForm):
    class Meta:
        model = Subject
        fields = ['name','start_date','description','level']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'start_date': forms.TextInput(attrs={'class': 'datepicker-default form-control'}),
            'description': forms.TextInput(attrs={'class': 'form-control'}),
            'level': forms.Select(attrs={'class': 'form-control'}),
        }

class StudentForm(forms.ModelForm):
    class Meta:
        model = Students
        fields = ['first_name','last_name','birthdate','mail','phone_number','status']
        widgets ={
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'birthdate': forms.TextInput(attrs={'class': 'datepicker-default form-control'}),
            'mail': forms.TextInput(attrs={'class': 'form-control'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control'}),
            'status': forms.TextInput(attrs={'class': 'form-control'}),
        }