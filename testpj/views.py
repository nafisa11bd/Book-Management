from django.http import HttpResponse
from django.shortcuts import render

def shama(request):
    return HttpResponse("Hello Shama")
def home(request):
    return render (request,"index.html")