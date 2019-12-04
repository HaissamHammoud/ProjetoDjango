from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home_view(request,*args , **kwargs):
    #return HttpResponse("<h1> ols mundo </h1>")
    return render(request , "home.html", {})

def pag2(request ,*args, **kwargs):
    return render(request,"memoria/JogoDaMemoria.html" , {})
