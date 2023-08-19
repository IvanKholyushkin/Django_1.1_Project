from django.shortcuts import render

from django.http import HttpResponse

from books.models import Book


def books_view(request):
    template = 'books/books_list.html'
    context = {'books': Book.objects.all()}
    return render(request, template, context)


def catalog_view(request):
    books = Book.objects.all()
    return HttpResponse(books)
