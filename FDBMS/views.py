from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .data import details
import pandas as pd

def index(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        print(email, password)
        
        user = authenticate(username=email, password=password)
        
        if user is not None:
            login(request, user)
            messages.success(request, "Successfully Logged In")
            return redirect('get')
        else:
            messages.error(request, "Invalid Credentials")
            return redirect('')
    return redirect('signin')

def signin(request):
    print(request.method)
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        print(email, password)
        
        user = authenticate(username='rprem058@gmail.com', password='aaaaa')
        
        if user is not None:
            login(request, user)
            messages.success(request, "Successfully Logged In")
            return redirect('get')
        else:
            messages.error(request, "Invalid Credentials")
            return redirect('signin')
    return render(request, "signin.html")

def signup(request):
    
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        myuser = User.objects.create_user(email, email, password)
        
        myuser.save()
        
        messages.success(request, "Your account has been successfully created")
        
        return redirect('signin')
    
    return render(request, "signup.html")

def get(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        data = details.getdetails(email)
        print(data)
        return render(request, "get.html", data)
    data = details.alldetails()
    return render(request, "get.html", data)

def set(request):
    if request.method == 'POST':
        id = request.POST.get('id')
        name = request.POST.get('name')
        pos = request.POST.get('pos')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        
        
        data = {
        'Faculty ID': id,
        'Faculty Name': name,
        'Position': pos,
        'Contact Number': phone,
        'Email ID': email
        }
        print(data)
        
        details.store(data)
        
        data = details.getdetails(email)
        
        return render(request, "set.html", data)
    data = details.alldetails()
    return render(request, "set.html", data)