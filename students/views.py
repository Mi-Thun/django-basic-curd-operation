from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import User

def home(request):
    return HttpResponse("Hello World")


def student(request, name):
    return HttpResponse(name)


def add_student(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        
        user = User(name=name, email=email)
        user.save()

        return redirect('/')
    
    return render(request, 'add.html')