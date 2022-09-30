from operator import ge
from django import forms
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic.base import TemplateView
from django.views.generic import View
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.views.generic import View
from .forms import LoginForm
from django.views.generic import FormView, RedirectView
from django.contrib.auth.views import LogoutView
from .forms import (
    StudentAcc,
    StudentForm,
    TeacherAcc,
    TeacherForm,
    Standard,
    StandardForm,
)
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import CreateView
from django.contrib.auth import login
from django.contrib.auth import authenticate, login, logout
from django import forms

# Create your views here.
# Signup
class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login_url")
    template_name = "registration/signup.html"


class HomeView(TemplateView):
    template_name = "base.html"


# login
class LoginPageView(View):
    template_name = "registration/login.html"
    form_class = LoginForm

    def get(self, request):
        form = self.form_class()
        # message = ""
        return render(request, self.template_name, context={"form": form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            print("#####")

            user = authenticate(
                username=form.cleaned_data["username"],
                password=form.cleaned_data["password"],
            )
            print("&&&&&&&&&&&&&&")
            if user is not None:
                print("*********")
                print(user)
                login(request, user)
                return redirect("std_url")

            # message = "Login failed!"
            print("###########")
            print(user)

            return render(request, self.template_name, context={"form": form})


# logout
class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect("login_url")


###for Form


# class homeView(TemplateView):
#     template_name = "base.html"
# Standard


class StandardView(CreateView):
    model = Standard
    fields = "__all__"
    template_name = "registration/stustandard.html"
    success_url = reverse_lazy("stuf_url")


class Show_standard(ListView):
    model = Standard
    template_name = "registration/standardshow.html"


class Update_standard(UpdateView):
    model = Standard
    fields = "__all__"
    template_name = "registration/stdupdate.html"
    success_url = "/showstd/"


class Del_standard(DeleteView):
    model = Standard
    template_name = "registration/stdconfirmation.html"
    success_url = "/showstd/"


# Student


class StudentfView(CreateView):
    model = StudentAcc
    fields = "__all__"
    template_name = "registration/studentacc.html"
    # success_url = '/app1/show'
    success_url = reverse_lazy("show")


class Show_Student(ListView):
    model = StudentAcc
    template_name = "registration/studshow.html"


class Update_student(UpdateView):
    model = StudentAcc
    fields = "__all__"
    template_name = "registration/stuupdate.html"
    success_url = "/show/"


class Del_student(DeleteView):
    model = StudentAcc
    template_name = "registration/confirmation.html"
    success_url = "/show/"


# Teacher


class TeacherfView(CreateView):
    model = TeacherAcc
    fields = "__all__"
    template_name = "registration/teacheracc.html"
    success_url = reverse_lazy("showt")


class Show_Teacher(ListView):
    model = TeacherAcc
    template_name = "registration/teachershow.html"


class Update_teacher(UpdateView):
    model = TeacherAcc
    fields = "__all__"
    template_name = "registration/teacherupdate.html"
    success_url = "/showt/"


class Del_teacher(DeleteView):
    model = TeacherAcc
    template_name = "registration/teacherconfirmation.html"
    success_url = "/showt/"
