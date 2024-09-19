from django.shortcuts import render

import requests

# Create your views here.
endpoint = 'http://localhost:4000/'

def index(request):
    return render(request, 'index.html')

def login(request):
    return render(request, 'login.html')

def register(request):
    return render(request, 'register.html')