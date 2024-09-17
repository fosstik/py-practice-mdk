from django.shortcuts import redirect, render, reverse
from django.db.models import Q
from practic4.models import Book

def search_book(req):
    if req.method == "GET":
        search = req.GET['search']
        books = Book.objects.filter(
            Q(title_icontains = search) | Q(author__name__icontains = search)) 
        return render(req, template_name="layout.html", context={
            'books': books,
            'title': 'Книги'
    } )
    return redirect(reverse('home'))