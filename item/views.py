# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from .models import *
from django.db.models import Q

# Create your views here.
def index(request):

    response = {}
    return render(request, 'item/index.html', response)

def get_travel_data(request, region_selected=None):
    datas = None
    try:
        datas = Itinerary.objects.filter(region = region_selected).order_by('departure_date')
    except Exception as e:
        print(e)
    return render(request, 'item/region.html', {'datas': datas, 'region':region_selected})

def search_result(request):
    datas=None
    region = request.GET.get("region")
    startDate = request.GET.get("StartDate")
    endDate = request.GET.get("EndDate")
    keyWords = request.GET.get("KeyWords")
    try:
        datas = Itinerary.objects.filter(Q(region__contains = region)&
                                         Q(departure_date__range=(startDate, endDate))&
                                         Q(title__icontains = keyWords)).order_by('departure_date')
    except Exception as e:
        print(e)
    return render(request, 'item/region.html', {'datas': datas})
