from django.shortcuts import render
from django.shortcuts import HttpResponse

# Create your views here.
# Request -> Responses
# Request Handlers

def hello(request):
    return render(request, 'app.html')

def say_hello(request):
    return HttpResponse("Halo Dunia")