from django.shortcuts import render
from django.http import HttpResponse
from .models import Booking
from .serializers import bookingSerializer
from datetime import datetime  
from .models import MenuItem
from .serializers import MenuItemSerializer
from rest_framework import generics

# Create your views here.
def home(request): 
    return render(request, 'home.html')


class MenuItemsView(generics.ListCreateAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer

class SingleMenuItemView(generics.RetrieveUpdateDestroyAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer