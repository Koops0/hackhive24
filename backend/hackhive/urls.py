from django.urls import path
from .views import CalendarView

urlpatterns = [
    path('home/', CalendarView.as_view()),
]