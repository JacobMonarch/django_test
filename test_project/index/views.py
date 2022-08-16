from django.shortcuts import render
from jinja2 import Template

# Create your views here.
def first(request):
    return render(request, 'index.html')
