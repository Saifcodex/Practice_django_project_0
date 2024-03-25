from django.shortcuts import render
from . import forms
# Create your views here.
def add_product(request):
    if request.method="POST":
        form = forms.ProductForm(request.POST)