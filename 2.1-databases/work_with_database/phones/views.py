import csv

from django.shortcuts import render, redirect

from phones.models import Phone


def index(request):
    return redirect("catalog")


def show_catalog(request):
    phones = Phone.objects.all()
    context = request.GET.get('sort')
    if context == 'name':
        context = {'phones': phones.order_by('name')}
        return render(request, "catalog.html", context)
    elif context == 'min_price':
        context = {'phones': phones.order_by('price')}
        return render(request, "catalog.html", context)
    elif context == 'max_price':
        context = {'phones': phones.order_by('-price')}
        return render(request, "catalog.html", context)
    else:
        context = {'phones': phones}
        return render(request, "catalog.html", context)


def show_product(request, slug):
    context = {'phone': Phone.objects.filter(slug__iexact=slug).values()[0]}
    return render(request, "product.html", context)
