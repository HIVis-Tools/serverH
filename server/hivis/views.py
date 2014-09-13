from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader

def index(request):
    return HttpResponse("Hello, world. You're at the HIVIS index.")

def alignment(request):
    resultdata = {"ref":1, "query":2}
    context = {'resultdata': resultdata}
    return render(request, 'hivis/alignment.html', context)
