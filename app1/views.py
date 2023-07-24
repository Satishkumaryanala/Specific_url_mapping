from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def first(request):
    return HttpResponse('<h1>This is specific url response for app1 first</h1>')


def second(request):
    return HttpResponse('<h1>This is specific url response for app1 second</h1>')