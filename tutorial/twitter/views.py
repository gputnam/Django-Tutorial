from django.http import HttpResponse
from django.shortcuts import render
from forms import *

# Create your views here.

def makeuser(request):
    if request.method == 'POST':
	form = UserForm(request.POST)
	if form.is_valid():
	    form.save()
	    return HttpResponse('Thank You!')

    else:
	form = UserForm()
    return render(request,'form.html',{'form':form}) 


