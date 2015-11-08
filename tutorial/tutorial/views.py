from django.http import HttpResponse
from django.shortcuts import render
import datetime

def hello(request):
    return HttpResponse("Hello World")

def home(request):
    name = "Gray Putnam"    

    return render(request, 'home.html', {'name':name})



