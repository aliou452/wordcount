from django.http import HttpResponse
from django.shortcuts import render

def homepage(request):
    return render(request, 'home.html', {'Great': 'Nice to see you again'})

def count(request):
    return render(request, 'count.html')