from rest_framework import serializers
from .models import Calendar

#Calendar and Event serializers, event for workout
class CalendarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Calendar
        fields = '__all__'

class UpdateCalendarSerializer(serializers.ModelSerializer):
    code = serializers.CharField(validators=[])

    class Meta:
        model = Calendar
        fields = '__all__'