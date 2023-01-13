from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.template import loader
from .models import ProductInfo, ShopProducts ,Cart

# Create your views here.
def index(request):
    template = loader.get_template('index.html')
    product = ProductInfo.objects.all()
    cart = Cart.objects.get(id=1)
    context = {
        'products':product,
        'cartNum': cart
    }
    return HttpResponse(template.render(context))

def about(request):
    template = loader.get_template('about.html')
    return HttpResponse(template.render())

def shop(request):
    template = loader.get_template('shop.html')
    s_prods = ShopProducts.objects.all()
    context = {
        'shopProducts':s_prods
    }
    return HttpResponse(template.render(context))

def contact(request):
    template = loader.get_template('contact.html')
    return HttpResponse(template.render())

def shop_single(request):
    template = loader.get_template('shop-single.html')
    return HttpResponse(template.render())

def addtocart(request):
    cart = Cart.objects.get(id=1)
    cart.cartCount += 1
    cart.save()
    return HttpResponseRedirect(reverse(shop))


def addtocartFromIndex(request):
    cart = Cart.objects.get(id=1)
    cart.cartCount += 1
    cart.save()
    return HttpResponseRedirect(reverse(index))
