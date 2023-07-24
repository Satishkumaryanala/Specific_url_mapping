from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def first(request):
    return HttpResponse('<h1><i>This is specific url response for app2 first</i></h1>')

def second(request):
    return HttpResponse('<h1><i> This is sepcefic url response for app2 second</i></h1>')