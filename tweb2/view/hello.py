#!/usr/bin/env python3
# -*- coding: utf-8 -*-

''

__author__ = 'Taburiss';

from django.http import HttpResponse


def hello(request):
	return HttpResponse("Hello World !")
