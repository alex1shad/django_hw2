import csv

from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.urls import reverse
from pagination.settings import BUS_STATION_CSV


with open(BUS_STATION_CSV, 'r', encoding='utf8') as file:
    new_rows_list = []
    for row in csv.reader(file):
        new_rows_list.append([row[1], row[4], row[6]])


def index(request):
    return redirect(reverse('bus_stations'))


def bus_stations(request):
    page_number = request.GET.get('page', 1)
    paginator = Paginator(object_list=new_rows_list[1:], per_page=10)
    page = paginator.get_page(page_number)
    context = {
        'bus_stations': page.object_list,
        'page': page
    }
    return render(request, 'stations/index.html', context)
