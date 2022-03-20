from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse('<h1>  Poha</h1>' '<h2>  Poha</h2>' '<h3>  Poha</h3>')