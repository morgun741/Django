from django.shortcuts import render
import json
from .models import Product
def products_list_views(request):
    #with open('products/fixtures/data/data.json') as file :
        #data = json.load(file)
    data = Product.objects.all()
    return render(request, 'products\index.html', {'object_list': data})
def product_ditail_view(request, pk):
    #with open('products/fixtures/data/data.json') as file :
        #data = json.load(file)
    data = Product.objects.get(pk=pk)
    return render(request, 'products\detail.html', {'object':data})
