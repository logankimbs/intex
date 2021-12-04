from django.shortcuts import render
from django.http import HttpResponse
from .models import Drugs
import re


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

    # convert all caps to normal
    text = 'AMLODIPINE.BESYLATE.BENAZEPRIL'.lower()
    punc_filter = re.compile('([.!?]\s*)')
    split_with_punctuation = punc_filter.split(text)
    final = ''.join([i.capitalize() for i in split_with_punctuation])
    print(final)

    return render(requests, 'portal/drugs.html', {'drugs': drugs})


# this page shows a detailed view of a specific drug
def viewdrugPageView(requests, drugname):
    drug = Drugs.objects.get(drugname=drugname)

    return render(requests, 'portal/viewdrug.html', {'drug': drug})
