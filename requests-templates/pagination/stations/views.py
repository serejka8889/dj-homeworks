from django.shortcuts import render, redirect
from django.urls import reverse

import csv
from django.conf import settings
from django.core.paginator import Paginator


def index(request):
    return redirect(reverse('bus_stations'))


def bus_stations(request):
    # получите текущую страницу и передайте ее в контекст
    # также передайте в контекст список станций на странице

    with open(settings.BUS_STATION_CSV, 'r', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        stations = list(reader)

    page = request.GET.get('page', 1)
    paginator = Paginator(stations, 12) 

    stations_page = paginator.get_page(page)
    page = paginator.get_page(page)

    context = {
        'bus_stations': stations_page,
        'page': page,
    }

    return render(request, 'stations/index.html', context)
