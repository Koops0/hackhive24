from django.db import models
import string
import random

# Create your models here.
#Calendar Model that displays the entire calendar for fitness app.
#Should display the calendar itself, events and details are for another class.

class Calendar(models.Model):
    month = models.PositiveIntegerField()
    year = models.PositiveIntegerField()
    events = models.ManyToManyField('Event', related_name='calendar_events', blank=True)

    def __str__(self):
        return f"{self.get_month_display()} {self.year}"

    def go_to_previous_month(self):
        self.month -= 1
        if self.month == 0:
            self.month = 12
            self.year -= 1
        self.save()

    def go_to_next_month(self):
        self.month += 1
        if self.month == 13:
            self.month = 1
            self.year += 1
        self.save()

class Event(models.Model):
    title = models.CharField(max_length=100)
    date = models.DateField()
    description = models.TextField()

    def __str__(self):
        return self.title