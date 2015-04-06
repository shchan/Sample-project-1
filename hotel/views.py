from django.shortcuts import render
from django.http import HttpResponse

from .models import Hotel

def index(request):
    context = {'hotels': Hotel.objects.all()}
    return render(request, 'hotel/index.html', context)
