from django.db import models
from datetime import date
import string
import random

# Create your models here.
#Calendar Model that displays the entire calendar for fitness app.
#Should display the calendar itself, events and details are for another class.
    
class Calendar(models.Model):
    title = models.CharField(max_length=100, default = 'Legs')
    month = models.PositiveIntegerField(choices=[(i, i) for i in range(1, 13)])
    day_of_workout = models.PositiveIntegerField(choices=[(i, i) for i in range(1, 32)], default = 1)
    year = models.PositiveIntegerField()
    #For events, make a textbox for events, and then display them on the calendar.
    description = models.TextField(max_length=280, default='Put workouts here')

    def __str__(self):
        return f"{self.get_month_display()} {self.year}"

    def go_to_previous_month(self):
        self.month -= 1
        if self.month == 0:
            self.month = 12
            self.day_of_workout = 31
            self.year -= 1
        self.save()

    def go_to_next_month(self):
        self.month += 1
        if self.month == 13:
            self.month = 1
            self.day_of_workout = 1
            self.year += 1
        self.save()