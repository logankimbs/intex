from django.shortcuts import render
from django.http import HttpResponse


def indexPageView(requests):
    return render(requests, 'portal/index.html')


# this page displays all prescribers in a table
def prescribersPageView(requests):
    return render(requests, 'portal/prescribers.html')


# this page shows a detailed view of a specific prescriber
def viewPrescriberPageView(requests):
    return render(requests, 'portal/viewprescriber.html')


# this page allows user to edit a specific prescriber
def editPrescriberPageView(requests):
    return render(requests, 'portal/editprescriber.html')


# this page allows user to create a prescriber
def createPrescriberPageView(requests):
    return render(requests, 'portal/createprescriber.html')
