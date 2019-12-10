from django.shortcuts import render
from .models import Product
from .forms import  ProductForm
# Create your views here.


def product_create_view(request):
    context = {}
    return render(request, "products/product_create.html", context)

#este é um metodo ultilizando formulario html puro
#Nao recomendado


# def product_create_view(request):
#     if request.method == "POST":
#
#         new_title = request.POST.get('title')
#         Product.objects.create(title = new_title)
#     context = {}
#     return render(request, "products/product_create.html", context)

#este é um metodo pronto que cria um formulario ja pre montado
#bom para agilidae e prototipos  pois economisa tempo e facilita o teste

# def product_create_view(request):
#     form = ProductForm(request.POST or None )
#     if form.is_valid():
#         form.save()
#
#     context = {
#     'form': form
#     }
#     return render(request, "products/product_create.html", context)



def product_detail_view(request):
    obj = Product.objects.get(id=1)
    context = {
    'object' : obj,
    }
    return render(request,"products/detail.html", context)
