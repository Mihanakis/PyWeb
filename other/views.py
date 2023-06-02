from django.shortcuts import render

from datetime import datetime
from django.views import View
from django.http import HttpResponse
from random import random

random_number = random()


class CurrentDateView(View):
    def get(self, request):
        html = f'{datetime.now()}'
        return HttpResponse(html)


class RandomNumber(View):
    def get(self, request):
        html = f'{random_number}'
        return HttpResponse(html)


class HelloWorld(View):
    def get(self, request):
         html = "<h1>Hello World<h1>"
         return HttpResponse(html)
