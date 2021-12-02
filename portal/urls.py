from django.urls import path
from .views import indexPageView
from .views import prescribersPageView
from .views import viewPrescriberPageView
from .views import editPrescriberPageView
from .views import createPrescriberPageView

urlpatterns = [
    path('', indexPageView, name='index'),
    path('prescribers/', prescribersPageView, name='prescribers'),
    path('viewprescriber/', viewPrescriberPageView, name='viewprescriber'),
    path('editprescriber/', editPrescriberPageView, name='editprescriber'),
    path('createprescriber/', createPrescriberPageView, name='createprescriber'),
]
