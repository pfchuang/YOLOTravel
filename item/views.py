# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
# from django.template import RequestContext, loader
from .models import *
from functools import reduce
import operator
from django.db.models import Q
import ast

# Create your views here.

def index(request):

    response = {}
    return render(request, 'item/index.html', response)

def get_travel_data(request, region_selected=None):
    datas = None
    try:
        datas = Itinerary.objects.filter(region = region_selected).order_by('-id')
        travel_dates = Travel_Date.objects.filter(itinerary__in=datas)
    except Exception as e:
        print(e)
    return render(request, 'item/region.html', {'datas': datas, 'region':region_selected, 'travel_dates': travel_dates})

def search_result(request):
    datas=None
    region = request.GET.get("region")
    startDate = request.GET.get("StartDate")
    endDate = request.GET.get("EndDate")
    # keyWords = request.GET.get("KeyWords")
    search = request.GET.get("KeyWords").split(' ')
    keyWords = reduce(operator.or_, (Q(title__icontains=x) for x in search))

    try:
        datas = Itinerary.objects.filter(Q(region__contains = region)&
                                         Q(travel_date__departure_date__range=(startDate, endDate))&
                                         Q(keyWords)).order_by('-id').distinct()
        travel_dates = Travel_Date.objects.filter(itinerary__in=datas)
    except Exception as e:
        print(e)
    return render(request, 'item/region.html', {'datas': datas, 'travel_dates': travel_dates})

def data_detail(request, id):
    data = Itinerary.objects.get(id = id)
    detail = ast.literal_eval(data.detailed)
    travel_dates = Travel_Date.objects.filter(itinerary=data)
    return render(request, 'item/detail.html', locals())