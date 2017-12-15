#!/usr/bin/env python3
# -*- coding: utf-8 -*-

''

__author__ = 'Taburiss';

from django.http import JsonResponse
from django.shortcuts import render
import base64



def b64(request):
    context = {}
    context['title'] = 'B64'
    return render(request, 'tool/b64.html', context)

def b64Encode(request):
    if request.method == 'POST':
        s = request.POST['plain']
        r = base64.b64encode(s.encode('utf-8'))
        return  JsonResponse({'cipher':r.decode()})

def b64Decode(request):
    if  request.method == 'POST':
        s = request.POST['cipher']
        r = base64.b64decode(s.encode('utf-8'))
        return JsonResponse({'plain': r.decode()})

def index(request):
    context = {}
    context['title'] = 'Tool'
    return render(request, 'tool/index.html', context)