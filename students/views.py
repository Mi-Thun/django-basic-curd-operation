from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import User

def add_student(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        
        student = User(name=name, email=email)
        student.save()

        return redirect('/')
    return render(request, 'add.html')


def view_student(request):
    students = User.objects.all()
    return render(request, 'index.html', {'students': students})


def edit_student(request, student_id):
    student = User.objects.get(id=student_id)

    if request.method == 'POST':
        student.name = request.POST['name']
        student.email = request.POST['email']
        student.save()

        return redirect('/') 

    return render(request, 'edit.html', {'student': student})