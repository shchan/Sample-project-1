import logging

from datetime import date

from dateutil import parser

from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from django.views import generic
from psycopg2.extras import DateRange

from .models import Availability

LOG = logging.getLogger(__name__)


class IndexView(generic.ListView):
    template_name = 'listing/index.html'
    context_object_name = 'listings'

    def get_queryset(self):
        return Availability.objects.all()

class SearchView(generic.View):
    def get(self, request):
        form_data = request.GET
        check_in = form_data.get('checkIn')
        check_out = form_data.get('checkOut')

        log_search(check_in, check_out)

        in_date = parse_date(check_in)
        out_date = parse_date(check_out)
        date_range = DateRange(in_date, out_date)

        available = Availability.objects.filter(period__contains=date_range)
        available = available.select_related('room')

        log_results(available)

        context = {
            'form': form_data,
            'listings': available,
        }
        template_name = "listing/search.html"
        return render(request, template_name, context)

class DetailView(generic.DetailView):
    model = Availability
    template_name = 'listing/detail.html'

def parse_date(a_date):
    return parser.parse(a_date, default=date.today())

def log_search(check_in, check_out):
    LOG.info('event=search, check_in=%s, check_out=%s', check_in, check_out)

def log_results(results):
    LOG.info('event=search_result, result=%s', results)
