# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
# from django.template import RequestContext, loader
from .models import *
from functools import reduce
import operator
from django.db.models import Q
import ast
import jieba
import re

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
    detail = ast.literal_eval(data.detail)

    region = data.region
    clean_title = re.sub("[〈〉～《》▪￭◆．等日無天 A-Za-z0-9「」ｘ『』•【】\x08;\s+\.\!\<>/_,$%^*(+\"\'+——！，\[\]Xx｜。１２３４５６７８９？、~@#￥%……&*（）＋；〜－)®：●♥★™🏆‧-]",
        "", data.title)
    cut_title = jieba.lcut(clean_title)
    print(type(cut_title))
    travel_dates = Travel_Date.objects.filter(itinerary=data)
    travel_date = travel_dates[0]
    condition = reduce(operator.or_, (Q(detail__icontains = x) for x in cut_title))
    similar_data = Itinerary.objects.filter(condition)
    if len(similar_data) >0 and len(similar_data) >= 5:
        similar_data = similar_data[:5]
    elif len(similar_data) == 0:
        similar_data.append("敬請期待")
    return render(request, 'item/detail.html', locals())