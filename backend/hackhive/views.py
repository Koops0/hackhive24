from django.shortcuts import render
from rest_framework import generics
from .serializers import CalendarSerializer
from .models import Calendar
# Create your views here.

#Calendar view
class CalendarView(generics.CreateAPIView):
    queryset = Calendar.objects.all()
    serializer_class = CalendarSerializer
