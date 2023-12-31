import csv

from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.urls import reverse

from pagination import settings


def index(request):
    return redirect(reverse('bus_stations'))


def bus_stations(request):
    with open(settings.BUS_STATION_CSV, newline='', encoding='utf-8-sig') as csvfile:
        reader = csv.DictReader(csvfile)
        bus_stations = []
        for row in reader:
            bus_stations.append({'Name': row["Name"], 'Street': row["Street"], 'District': row["District"]})

    page_number = int(request.GET.get('page', 1))
    paginator = Paginator(bus_stations, 10)
    page = paginator.get_page(page_number)

    context = {
        'bus_stations': page.object_list,
        'page': page,
    }
    return render(request, 'stations/index.html', context)
