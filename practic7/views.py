from django.shortcuts import render

def main(req):
    return render(req, 'pr7_index.html')

def about(req):
    return render(req, 'pr7_about.html')

def products(req):
    return render(req, 'pr7_products.html')