from django.shortcuts import render
from django.http import HttpResponse
from .models import Drugs, Prescribers, State
import re


# this page displays our home page
def indexPageView(requests):
    return render(requests, 'portal/index.html')


# this page displays extra info about the opioid epidemic and prescribers of opioids
def aboutPageView(requests):
    return render(requests, 'portal/about.html')


# this page displays all prescribers in a table
def prescribersPageView(requests):
    prescribers = Prescribers.objects.all()

    return render(requests, 'portal/prescribers.html', {'prescribers': prescribers})


# this page shows a detailed view of a specific prescriber
def viewPrescriberPageView(requests, npi):
    prescriber = Prescribers.objects.get(npi=npi)

    return render(requests, 'portal/viewprescriber.html', {'prescriber': prescriber})


# this page allows user to edit a specific prescriber
def editPrescriberPageView(requests, npi, fname, lname):
    prescriber = Prescribers.objects.get(npi=npi)
    states = State.objects.all()

    return render(requests, 'portal/editprescriber.html', {'prescriber': prescriber, 'states': states})


# this page allows user to create a prescriber
def createPrescriberPageView(requests):
    return render(requests, 'portal/createprescriber.html')


# this page displays all drugs in a table
def drugsPageView(requests):
    return render(requests, 'portal/drugs.html')


# this page shows a detailed view of a specific drug
def viewdrugPageView(requests):
    return render(requests, 'portal/viewdrug.html')
