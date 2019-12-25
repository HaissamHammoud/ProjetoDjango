from django.shortcuts import render
from .models import Car
from .forms import CarForms

# Create your views here.
def car_entrance(request):
    form = CarForms(request.POST or None)
    if form.is_valid():
        form.save()

    context = {
        'form':form
    }

    return render(request , "carros/Entrada.html",context)

def car_exit(request):
    return render(request,"carros/saida.html", {})

def car_menu(request):
    return render(request, "menu.html")
