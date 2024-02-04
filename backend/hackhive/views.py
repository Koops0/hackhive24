from django.shortcuts import render
from rest_framework import viewsets
from .serializers import CalendarSerializer
from .models import Calendar


# Create your views here.

#Calendar view
class CalendarView(viewsets.ModelViewSet):
    queryset = Calendar.objects.all()
    serializer_class = CalendarSerializer