
from django.shortcuts import render
from .models import Product

# def product_list(request):
#     products = Product.objects.all()  # Fetch all products
#     return render(request, 'product.html',{'products':products})

from django.shortcuts import render
from .models import Product

def product_list(request):
    products = Product.objects.prefetch_related('images').all()  # Fetch products with images efficiently
    return render(request, 'product.html', {'products': products})

