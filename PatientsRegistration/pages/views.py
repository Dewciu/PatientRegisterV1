
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home_view(*args, **kwargs):
    return HttpResponse("<h1>Hello! I'm currently learing about coding with python in django! Here will be some functional patient registration site :D</h1>")

def register_view(*args, **kwargs):
    return HttpResponse("<h1>Register View</h1>")

def contact_view(*args, **kwargs):
    return HttpResponse("<h1>Contact Page</h1>")

