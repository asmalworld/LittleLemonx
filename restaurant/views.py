from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response 
from .serializers import bookingSerializer, MenuSerializer
from rest_framework import viewsets 
from .models import Menu, Booking
from rest_framework import generics
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser

# Create your views here.
def home(request): 
    return render(request, 'home.html')

class MenuView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated, IsAdminUser]
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

class SingleMenuView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated, IsAdminUser]
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

class BookingViewSet(viewsets.ReadOnlyModelViewSet):
    permission_classes = [IsAuthenticated, IsAdminUser]
    queryset = Booking.objects.all()
    serializer_class = bookingSerializer