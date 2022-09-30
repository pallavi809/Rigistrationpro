from django import forms
from django.forms import PasswordInput
from .models import LoginModel
from .models import TeacherAcc, StudentAcc, Standard

# Login
class LoginForm(forms.ModelForm):
    class Meta:
        model = LoginModel
        fields = "__all__"
        widgets = {"password": forms.PasswordInput(attrs={"class": "myclass"})}


# Standard
class StandardForm(forms.ModelForm):
    class Meta:
        model = Standard
        fields = "__all__"


# Student
class StudentForm(forms.ModelForm):
    class Meta:
        model = StudentAcc
        fields = "__all__"
        labels = {
            "rollnum": "Roll Number",
            "name": "Name",
            "email": "Email Id",
            "phonenum": "Phone Number",
            "attendance": "Attendance",
        }
        widgets = {
            "rollnum": forms.NumberInput(attrs={"placeholder": "eg 1"}),
            "name": forms.TextInput(attrs={"placeholder": "eg joe"}),
            "email": forms.EmailInput(attrs={"placeholder": "eg joe@gmail.com"}),
            "phonenum": forms.NumberInput(attrs={"placeholder": "eg +916765434589"}),
            "attendance": forms.TextInput(attrs={"placeholder": "eg present"}),
        }


# Teacher
class TeacherForm(forms.ModelForm):
    class Meta:
        model = TeacherAcc
        fields = "__all__"
