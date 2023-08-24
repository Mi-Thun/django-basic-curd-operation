from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse("Hello World")


def student(request, name):
    return HttpResponse(name)