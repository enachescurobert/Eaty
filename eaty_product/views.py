from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.generic.base import TemplateView
from rest_framework import viewsets
from eaty_product.models import ProductType, Product
from eaty_product.serializers import ProductTypeSerializer, ProductSerializer
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser

class ProductTypeViewSet(viewsets.ModelViewSet):
    """ ViewSet for viewing and editing ProductType objects """
    queryset = ProductType.objects.all()
    serializer_class = ProductTypeSerializer

class ProductViewSet(viewsets.ModelViewSet):
    """ ViewSet for viewing and editing Product objects """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

# def index(request):
#     #return HttpResponse("You are at /Product/ index")
#     return render(request, 'index.html')
#     #template = loader.get_template('eaty_product/index.html')


# @csrf_exempt
# def products_list(request):
#     """
#     List all code products, or create a new product.
#     """
#     if request.method == 'GET':
#         products = ProductType.objects.all()
#         serializer = ProductTypeSerializer(products, many=True)
#         return JsonResponse(serializer.data, safe=False)

#     elif request.method == 'POST':
#         data = JSONParser().parse(request)
#         serializer = ProductTypeSerializer(data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data, status=201)
#         return JsonResponse(serializer.errors, status=400)