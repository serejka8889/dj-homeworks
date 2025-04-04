from django.shortcuts import render, redirect
from .models import Phone
from django.shortcuts import get_object_or_404


def index(request):
    return redirect('catalog')


def show_catalog(request):
    template = 'catalog.html'
    
    sort_by = request.GET.get('sort', '')
    if sort_by == 'name':
        phones = Phone.objects.order_by('name')
    elif sort_by == 'min_price':
        phones = Phone.objects.order_by('price')
    else:
        phones = Phone.objects.all()  

    context = {'phones': phones}

    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'

    phone = get_object_or_404(Phone, slug=slug)
    
    context = {'phone': phone}

    return render(request, template, context)
