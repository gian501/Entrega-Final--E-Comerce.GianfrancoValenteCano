from django.shortcuts import render
from .models import Producto
# Create your views here.

def home(request):
    return render(request, 'AppEC/home.html')

def products(request):
    producto = Producto.objects.all()
    return render(request, 'AppEC/products.html', {'producto':producto})