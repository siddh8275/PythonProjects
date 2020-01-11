from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index():
    return HttpResponse("<H2> Welcome to first Django Project</H2>")