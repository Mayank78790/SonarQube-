from django.shortcuts import render, HttpResponse
# Create your views here.
# FBV

from django.http import HttpResponse

def testview(request):
    return HttpResponse("Hello from testview!")

def testhtml(request):
    return HttpResponse("<h1>Hello from testhtml!</h1>")
