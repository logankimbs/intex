from django.shortcuts import render
from django.http import HttpResponse


def indexPageView(requests):
    return render(requests, 'portal/index.html')
