from django.urls import path
from .views import CalendarView, UpdateCalendarView

urlpatterns = [
    path('calendar', CalendarView.as_view()),
    path('update-calendar', UpdateCalendarView.as_view()),
]