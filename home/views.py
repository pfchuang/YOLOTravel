# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from item.models import TopWord

# Create your views here.
def index(request):
    top_words = TopWord.objects.all()
    return render(request, 'home/index.html', {'top_words':top_words})
    # return render(request, 'home/index.html', response)
