from django.shortcuts import render
from django.http import HttpResponse
from .models import MenuItem
from .serializers import MenuItemSerializer


# Create your views here.
def index(request): 
    return render(request, 'index.html')