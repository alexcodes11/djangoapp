from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, "first/index.html")

def login(request):
    return render(request, "first/login.html")

def register(request):
    return render(request, "first/register.html")
