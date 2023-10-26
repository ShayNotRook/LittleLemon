from django.shortcuts import render
from rest_framework.response import Response
from .models import Menu, Booking
from .serializers import MenuSerializer, BookingSerializer
from rest_framework import generics, viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
# Create your views here.
def index(request):
    return render(request, 'index.html', {})
class MenuItemView(generics.ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    # permission_classes = [IsAuthenticated]
    
class SingleItemView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    
    
class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [IsAuthenticated]
    
@api_view()
@permission_classes([IsAuthenticated])

def msg(request):
    return Response({'message':'This view is protected'})
