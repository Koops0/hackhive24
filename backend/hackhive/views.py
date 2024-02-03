from django.shortcuts import render
from rest_framework import generics
from .serializers import CalendarSerializer, UpdateCalendarSerializer
from .models import Calendar
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import JsonResponse

# Create your views here.

#Calendar view
class CalendarView(generics.CreateAPIView):
    queryset = Calendar.objects.all()
    serializer_class = CalendarSerializer

class getCalendar(APIView):
    serializer_class = CalendarSerializer
    lookup = 'pk'

    def get(self, request):
        lookup = request.GET.get('pk')
        if lookup:
            calendar = Calendar.objects.filter(pk=lookup)
            if len(calendar) > 0:
                serializer = CalendarSerializer(calendar[0])
                return Response(serializer.data)
            else:
                return JsonResponse({'error': 'Calendar not found'})
        else:
            return JsonResponse({'error': 'No pk provided'})

class UpdateCalendarView(APIView):
    serializer_class = UpdateCalendarSerializer

    def patch(self, request):
        code = request.data.get('code')
        if code:
            calendar = Calendar.objects.filter(code=code)
            if len(calendar) > 0:
                calendar = calendar[0]
                serializer = UpdateCalendarSerializer(calendar, data=request.data)
                if serializer.is_valid():
                    serializer.save()
                    return JsonResponse({'success': 'Calendar updated'})
                else:
                    return JsonResponse({'error': 'Invalid data'})
            else:
                return JsonResponse({'error': 'Calendar not found'})
        else:
            return JsonResponse({'error': 'No code provided'})
    

        