from django.shortcuts import render
from .models import pr8_product

def index(req):
    books = pr8_product.objects.all()
    return render(req, 'pr8_index.html', context= {
        'books':books
    })