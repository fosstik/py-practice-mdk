from django.shortcuts import render,redirect, get_object_or_404
from .cart import CartSession
from django.http import HttpRequest
from practic7.models import Product

def cart_add(req: HttpRequest, product_id):
    cart = CartSession(req.session)
    product = get_object_or_404(Product, id=product_id)
    cart.add(product=product)
    return redirect('cart_detail')

def cart_remove(req:HttpRequest, product_id):
    cart = CartSession(req.session)
    product = get_object_or_404(Product, id=product_id)
    cart.remove(product=product)
    return redirect('cart_detail')

def cart_remove_all(req:HttpRequest): 
    cart = CartSession(req.session)
    cart.clear()
    return redirect('cart_detail')

def cart_detail(req: HttpRequest):
    cart = CartSession(req.session)

    return render(req, 'pr14_cart_detail.html', context={
        'cart':cart
    })


