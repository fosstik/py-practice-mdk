from django.shortcuts import render
from .models import Product

def main(req):
    return render(req, 'pr7_index.html')

def about(req):
    return render(req, 'pr7_about.html')

def products(req):
    products = Product.objects.all()
    return render(req, 'pr7_products.html', context ={
        'products': products
    })

def get_product_detail(req, pk):
    productDetail = Product.objects.get(pk = pk)
    return render(req, 'pr7_productPage.html', context = {
        'productDetail':productDetail
    })