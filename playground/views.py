from django.shortcuts import render
from django.shortcuts import HttpResponse

# Create your views here.
# Request -> Responses
# Request Handlers

def calculate():
    x = 1
    y = 2
    return x

def hello(request):
    x = calculate()
    return render(request, 'app.html')

def say_hello(request):
    return HttpResponse("Halo Dunia")