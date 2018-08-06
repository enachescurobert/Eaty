from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.base import TemplateView


def index(request):
    #return HttpResponse("You are at /Product/ index")
    return render(request, 'index.html')
    #template = loader.get_template('eaty_product/index.html')
