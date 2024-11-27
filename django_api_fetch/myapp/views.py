from django.http import HttpResponse
from django.shortcuts import render
from .models import Product
from .serializers import ProductSerializer
from .api import fetch

def home(request):
    data = fetch()
    print(type(data))
    for item in data:
        serializer = ProductSerializer(data = item)
        if serializer.is_valid():
            serializer.save()
        print("error....",item['id'], serializer.errors)

    return HttpResponse('<h1>Hello world</h1>')

    # data = Product.objects.all()
    # return render(request, 'myapp/index.html', {'data': data})
    