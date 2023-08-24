from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import User

def add_student(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        
        user = User(name=name, email=email)
        user.save()

        return redirect('/')
    return render(request, 'add.html')


def view_student(request):
    students = User.objects.all()
    return render(request, 'index.html', {'students': students})