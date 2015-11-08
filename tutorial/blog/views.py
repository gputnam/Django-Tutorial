from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from forms import *

# Create your views here.

def blogform(request):
    if request.method == 'POST':
	form = BlogForm(request.POST)
	if form.is_valid():
	    form.save()
	    return HttpResponse('Thanks!!')

    else:
	form = BlogForm()

    return render(request, 'form.html',{'form':form})


