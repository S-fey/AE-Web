from django.shortcuts import render
from .models import Product
# Create your views here.
def home_view(request):
    return render(request, 'AEapp/home.html')

def about_view(request):
    return render(request, 'AEapp/about.html')

def contact_view(request):
    return render(request, 'AEapp/contact.html')

def product_view(request):
    products = Product.objects.all()  
    return render(request, 'AEapp/produtos.html',  {'Products': products})