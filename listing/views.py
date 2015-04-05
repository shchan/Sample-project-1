from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("hi")

def detail(request, listing_id):
    return HttpResponse("listing %s" % listing_id)
