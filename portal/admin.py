from django.contrib import admin
from .models import pd_drugs, pd_prescriber, pd_statedata

admin.site.register(pd_drugs)
admin.site.register(pd_prescriber)
admin.site.register(pd_statedata)
