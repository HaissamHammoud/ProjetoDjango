"""trydjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from pages.views  import home_view, contact_view,about_view,social_view
from products.views import product_dynamic_view , product_create_view, top_products, loja_view
from JogoMemoria.views import memoria_view
from estacionamento.views import *
urlpatterns = [
    path('', home_view ,name = "home"),
    path('admin/', admin.site.urls),
    path('contact/', contact_view , name ='contact'),
    path('about/',about_view,name = 'about'),
    path('social/', social_view, name = 'Social'),
    path('loja/product/detail/<int:my_id>',product_dynamic_view),
    path('loja/menu', loja_view,name = 'menu'),
    path('loja/product/create/', product_create_view, name = 'Create'),
    path('loja/product/top_products/',top_products, name = 'Create'),
    path('memoria/',memoria_view, name = 'jogo'),
    path('estacionamento/entrance/', car_entrance, name = "entrada"),
    path('estacionamento/exit/', car_exit, name = "saida"),
    path('estacionamento/',car_menu, name='menu'),
    path('estacionamento/exit/<int:my_id>',car_detail_view),

]
