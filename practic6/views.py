from django.shortcuts import render
from practic4.models import Book

def get_info(req):
    book = Book.objects.get(id=1)
    return render(req, 'pr6_index.html', context ={
        'book':book
    })
    
def get_author(req):
    book_author = Book.objects.filter(author__name='Александр Сергеевич Пушкин')
    return render(req, 'pr6_author.html', context ={
        'book_author':book_author
    })
