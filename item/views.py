# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render

from .models import *
# Create your views here.
def index(request):

    response = {}
    return render(request, 'item/index.html', response)

def get_travel_data(request, region_selected=None):
    datas = None    
    try:
        if region_selected == "NorthEastAsia":
            datas = NorthEastAsia.objects.all()
        elif region_selected == "Europe":
            datas = Europe.objects.all()
        elif region_selected == "Oceania":
            datas = Oceania.objects.all()
        elif region_selected == "Africa":
            datas = Africa.objects.all()
        elif region_selected == "China":
            datas = China.objects.all()
        elif region_selected == "MiddleAsia":
            datas = MiddleAsia.objects.all()
        elif region_selected == "SouthEastAsia":
            datas = SouthEastAsia.objects.all()
    except Exception as e:
        print(e)
    return render(request, 'region.html', {'datas': datas})
