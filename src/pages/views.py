from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home_view(request,*args , **kwargs):
    #return HttpResponse("<h1> ols mundo </h1>")
    return render(request , "home.html", {})

def contact_view(request ,*args, **kwargs):
    return render(request,"contact.html" , {})

def about_view(request, *args, **kwargs):
    my_context = {
        "my_text": "this is about us",
        "my numer": "9999-00000"
    }
    return render(request, "about.html", my_context)

def social_view(request, *args , **kwargs):
    return HttpResponse("<h1> Social Page</1>")
