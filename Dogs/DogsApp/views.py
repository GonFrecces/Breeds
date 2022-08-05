from django.shortcuts import render, redirect
from DogsApp.models import Breeds

# Create your views here.
def Breeds_Dogs(request):

    breeds = Breeds.objects.all()
    data = {'Breeds': breeds}
    return render(request,"Index.html",data)