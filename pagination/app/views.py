from django.core.paginator import Paginator
from django.shortcuts import render_to_response, redirect
from django.urls import reverse
from .settings import BUS_STATION_CSV
import csv
from urllib.parse import urlencode


def index(request):
    return redirect(reverse(bus_stations))


def bus_stations(request):
    articles = []
    with open(BUS_STATION_CSV, encoding='cp1251') as text:
        read = csv.DictReader(text)
        for row in read:
            articles.append({'Name': row['Name'], 'Street': row['Street'], 'District': row['District']})
    paginator = Paginator(articles, 20)
    current_page = request.GET.get('page', 1)
    page = paginator.get_page(current_page)
    prev_page, next_page = None, None
    if page.has_previous():
        prev_page = page.previous_page_number()
    if page.has_next():
        next_page = page.next_page_number()
    context = {
        'bus_stations': page,
        'current_page': page.number,
        'prev_page_url': f'?page={prev_page}',
        'next_page_url': f'?page={next_page}',
    }

    return render_to_response('index.html', context=context)





