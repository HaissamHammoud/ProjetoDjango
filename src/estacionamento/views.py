from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
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
    #HttpResponseRedirect(Car,My_id)
    context = {
        'car': Car
    }
    return render(request,"carros/saida.html",context)

def car_menu(request):
    return render(request, "menu.html")


def car_detail_view(request, my_id):
    obj = get_object_or_404(Car, id = my_id)
    context = {
    'object' : obj,
    }
    return HttpResponse(request,"carros/cardetail.html", context)
