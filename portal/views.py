from django.shortcuts import render
from django.http import HttpResponse
from .models import Drugs


# this page displays our home page


def indexPageView(requests):
    return render(requests, 'portal/index.html')


# this page displays extra info about the opioid epidemic and prescribers of opioids
def aboutPageView(requests):
    return render(requests, 'portal/about.html')


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


# this page displays all drugs in a table
def drugsPageView(requests):
    drugs = Drugs.objects.all()

    return render(requests, 'portal/drugs.html', {'drugs': drugs})


# this page shows a detailed view of a specific drug
def viewdrugPageView(requests, drugname):
    context = {"drug": drugname}

    return render(requests, 'portal/viewdrug.html', context)
