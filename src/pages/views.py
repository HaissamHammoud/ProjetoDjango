from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home_view(request,*args , **kwargs):



    my_context= {

    }
    return render(request , "home.html", {})

def contact_view(request ,*args, **kwargs):
    return render(request,"contact.html" , {})

def about_view(request, *args, **kwargs):
    my_context = {   #my_context esta eniando variaveis a pagina html
        "my_text": "aqui tem um texto sobre nos",
        "my_number": "9999-00000"
    }
    return render(request, "about.html", my_context) #my_context é uma lista de variaveis

def social_view(request, *args , **kwargs):
    return HttpResponse("<h1> Social Page</1>")
