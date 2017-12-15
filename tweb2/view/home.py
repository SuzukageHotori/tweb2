#!/usr/bin/env python3
# -*- coding: utf-8 -*-

''

__author__ = 'Taburiss';

from django.http import HttpResponse
from django.shortcuts import render



def index(request):
    context = {}
    context['title'] = 'Index'
    return render(request, 'home/index.html', context)