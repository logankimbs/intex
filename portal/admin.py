from django.contrib import admin
from .models import Drugs, State, Credentials, Prescribers, Triple


admin.site.register(Drugs)
admin.site.register(State)
admin.site.register(Credentials)
admin.site.register(Prescribers)
admin.site.register(Triple)
