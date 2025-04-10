from django.urls import path
from Produits.views import *
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    #path('',home,name='home')

    path('',Affichage.as_view(),name='affichage')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)