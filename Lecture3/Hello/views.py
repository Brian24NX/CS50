from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
# First branch
def index(request):
    return render(request, "Hello/index.html")
# User-defined branch
def brian(request):
    return HttpResponse("Hello, Brian!")
def david(request):
    return HttpResponse("Hello, David!")
# Templates branch
def greet(request, name):
        return render(request, "Hello/greet.html", {
        "name": name.capitalize()
    })