from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from catalog.models import Pets, Shelter

# Create your views here.
def index(request):
    template = loader.get_template('catalog.html')
    all_pets=Pets.objects.all()
    data = {"pets": all_pets }
    return HttpResponse(template.render(data))

def dogs(request):
    template = loader.get_template('catalog.html')
    all_pets=Pets.objects.filter(type=1)
    data = {"pets": all_pets }
    return HttpResponse(template.render(data))

def cats(request):
    template = loader.get_template('catalog.html')
    all_pets=Pets.objects.filter(type=2)
    data = {"pets": all_pets }
    return HttpResponse(template.render(data))

def parrots(request):
    template = loader.get_template('catalog.html')
    all_pets=Pets.objects.filter(type=3)
    data = {"pets": all_pets }
    return HttpResponse(template.render(data))

def contacts(request):
    template = loader.get_template('contacts.html')
    all_shelters = Shelter.objects.all()
    data = {"shelters" : all_shelters}
    return HttpResponse(template.render(data))

def pet(request, id):
    template = loader.get_template('pet.html')
    pet = Pets.objects.filter(id = id).first()
    data = {"pet" : pet}
    return HttpResponse(template.render(data))