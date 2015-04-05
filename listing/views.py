from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse

from .models import Availability

def index(request):
    context = {'listings': Availability.objects.all()}
    return render(request, 'listing/index.html', context)

def detail(request, listing_id):
    listing = get_object_or_404(Availability, pk=listing_id)
    context = {'listing': listing}
    return render(request, 'listing/detail.html', context)
