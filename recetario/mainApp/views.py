from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import *
from .models import *

# Create your views here.

def inicio(request):
    Recetas = receta.objects.all()
    return render(request, "index.html", {"recetas": Recetas})

def addReceta(request):
    if request.method == "POST":
        form = RecetaForm(request.POST, request.FILES)
        if form.is_valid():
            print("ES VALIDA")
            form.save()
            return redirect(inicio)
        else:
            print("NO ES VALIDA:")
            print(form.errors)
    else:
        form = RecetaForm()
    return render(request, "addreceta.html", {'form' : form})

def verReceta (request,id):
    print(id)
    Receta = receta.objects.filter(id=id)[0]
    ingredientes = Receta.ingredientes.split("\n")
    pasos = Receta.pasos.split("\n")
    return render(request, "vistareceta.html", {"receta":Receta, "ingredientes":ingredientes, "pasos":pasos})

def editReceta(request,id):
    print(id)
    Receta = receta.objects.filter(id=id)[0]
    if request.method == "POST":
        form = RecetaForm(request.POST, request.FILES, instance=Receta)
        if form.is_valid():
            print("ES VALIDA")
            form.save()
            return redirect(inicio)
        else:
            print("NO ES VALIDA:")
            print(form.errors)
    else:
        form = RecetaForm({"nombreReceta":Receta.nombreReceta,"ingredientes":Receta.ingredientes,"pasos":Receta.pasos,"autor":Receta.autor})
    return render(request, "editreceta.html", {'form' : form, "receta":receta})

def deleteReceta(request,id):
    print(id)
    receta.objects.filter(pk=id).delete()
    print(id, " Eliminado")
    return redirect(inicio)
