from django.shortcuts import render
from django.http import HttpResponse
from .models import Drugs, Prescribers, State
import re


# this page displays our home page
def indexPageView(request):
    return render(request, 'portal/index.html')


# this page displays extra info about the opioid epidemic and prescribers of opioids
def aboutPageView(request):
    return render(request, 'portal/about.html')


# this page displays all prescribers in a table
def prescribersPageView(request):
    prescribers = Prescribers.objects.all()

    return render(request, 'portal/prescribers.html', {'prescribers': prescribers})


# this page shows a detailed view of a specific prescriber
def viewPrescriberPageView(request, npi):
    prescriber = Prescribers.objects.get(npi=npi)

    return render(request, 'portal/viewprescriber.html', {'prescriber': prescriber})


# this page allows user to edit a specific prescriber
def editPrescriberPageView(request, npi, fname, lname):
    prescriber = Prescribers.objects.get(npi=npi)
    states = State.objects.all()

    return render(request, 'portal/editprescriber.html', {'prescriber': prescriber, 'states': states})


# this page allows user to create a prescriber
def createPrescriberPageView(request):
    states = State.objects.all()

    if request.method == 'POST':
        npi = int(request.POST.get('prescriberNPI'))
        state = State.objects.get(
            stateabbrev=request.POST.get('prescriberState'))

        # does npi exist
        if not Prescribers.objects.filter(npi=npi).exists():
            new_prescriber = Prescribers()
            new_prescriber.npi = npi
            new_prescriber.fname = request.POST.get('prescriberFirstName')
            new_prescriber.lname = request.POST.get('prescriberLastName')
            new_prescriber.gender = request.POST.get('prescriberGender')
            new_prescriber.state = state
            new_prescriber.npi = npi
            new_prescriber.specialty = request.POST.get('prescriberSpecialty')
            new_prescriber.totalprescriptions = request.POST.get(
                'prescriberTotalPrescriptions')
            new_prescriber.isopioidprescriber = request.POST.get(
                'authorization')
            new_prescriber.save()

    return render(request, 'portal/createprescriber.html', {'states': states})


# this page displays all drugs in a table
def drugsPageView(request):
    return render(request, 'portal/drugs.html')


# this page shows a detailed view of a specific drug
def viewdrugPageView(request):
    return render(request, 'portal/viewdrug.html')
