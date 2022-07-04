import imp
from multiprocessing import context
from tokenize import Name
from django import forms
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from .forms import (formname,studentform)
from .models import student
from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
# Create your views here.
def index_view(request):
    form = formname()
    if request.method == 'POST':
        form = formname(request.POST)
        if form.is_valid():
            form.save()

    #all = student.objects.all().order_by('Roll_no').exclude(Roll_no = '2')
    #print(all)

    #filter = student.objects.filter(Name = "Aryan Agrawal")
    #print("Aryan Agrawal",filter)

    #filter = student.objects.filter(Name = "Rishi Jaiswal")
    #print('Name',filter)

    #get = student.objects.get(Roll_no = '3')
    #print('Roll number:',get)

    #create = student.objects.create(Name = 'Vartika Sariwan',)
    

    context={
        "student":form,
        "Data":all,
    }
    return render(request, 'index.html',context)
def new_view(request):
    var = request.POST.get('input')
    print(var)
    return render(request,'new.html')
@login_required
def student_info(request):
    stu = student.objects.all()
    context={
        "student":stu
    }
    return render(request,'student.html',context)

def update(request, id):
    Student = student.objects.get(id=id)
    var = request.POST.get("Name")
    print(var)
    form = studentform(request.POST, instance=Student)
    if form.is_valid():
        form.save()
        return redirect("Homepage")
    context ={
        "student":Student,
    }
    return render(request, "edit.html", context)

def edit(request,id):
    stu = student.objects.get(id=id)
    return render(request,'edit.html',{'student':stu})

def delete(request, id):
    context ={}
    obj = student.objects.get(id=id)
    obj.delete()
    return redirect("student page")

class AdminLogin(LoginView):
    print("AMIT")
    template_name= 'login.html'


def signup_view(request):
    '''Function to create a new user'''
    if request.method == 'POST':
        firstname=request.POST.get('firstname')
        lastname=request.POST.get('lastname')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirmpassword = request.POST.get('confirmpassword')
        if password == confirmpassword:
            user = User.objects.create_user(
                first_name = firstname,
                last_name = lastname,
                username = username,
                email = email,
                password = password
            )
            messages.success(request, "User {username} Created")
        else:
            messages.error(request, "Invalid credentials")
    return render(request, 'signup.html')