from django.urls import path
from .views import indexPageView
from .views import aboutPageView
from .views import prescribersPageView
from .views import viewPrescriberPageView
from .views import editPrescriberPageView
from .views import createPrescriberPageView
from .views import drugsPageView
from .views import viewdrugPageView


urlpatterns = [
    path('about/', aboutPageView, name='about'),
    path('prescribers/', prescribersPageView, name='prescribers'),
    path('<int:npi>/', viewPrescriberPageView, name='viewprescriber'),
    path('<int:npi>/<str:fname>/<str:lname>/',
         editPrescriberPageView, name='editprescriber'),
    path('createprescriber/', createPrescriberPageView, name='createprescriber'),
    path('drugs/', drugsPageView, name='drugs'),
    path('<str:drugname>/', viewdrugPageView, name='viewdrug'),
    path('', indexPageView, name='index'),
]
