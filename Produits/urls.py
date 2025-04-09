from django.urls import path
from Produits.views import *

urlpatterns = [
    path('',home,name='home')
]