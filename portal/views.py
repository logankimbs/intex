from django.shortcuts import render
from portal.models import pd_drugs

# this page displays our home page


def indexPageView(requests):
    return render(requests, 'portal/index.html')

# this page displays extra info about the opioid epidemic and prescribers of opioids.


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


def drugsPageView(requests):
    drugs = pd_drugs.objects.all()

    return render(requests, 'portal/drugs.html', {'drugs': drugs})


def viewdrugPageView(requests):
    return render(requests, 'portal/viewdrug.html')
