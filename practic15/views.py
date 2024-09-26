from django.shortcuts import render, redirect
from django.http import HttpRequest
from models import OrderItem

@login_required(login_url='login')
def create_order(req:HttpRequest):
    cart = CartSession(req.session)
    if req.method == "POST":
        form = OrderForm(req.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.customer_user = req.user
            order.save()
            for item_cart in cart:
                OrderItem.objects.create(order=order, book=item_cart['book'], quantity=item_cart['quantity']).save()
                cart.clear()
                return redirect('profile')

