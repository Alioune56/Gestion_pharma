from django.shortcuts import render
from .models import *

from django.views.generic import ListView

# Create your views here.
def home(request):

    # Recuperations des donnees de la bd
    #donnees = Produits.objects.all()

    #context = {
    #    'donnees':donnees
    #}

    return render(request,"home.html")

class Affichage(ListView):
    # Affichage du template
    template_name = 'home.html'
    # Recuperer les donnees de la bd
    queryset = Produits.objects.all()
