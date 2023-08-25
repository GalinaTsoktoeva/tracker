from rest_framework import serializers

from habit.models import Habit
from habit.validators import PleasantValidator


class PleasureHabitSerializer(serializers.ModelSerializer):

    class Meta:
        model = Habit
        fields = ('user', 'place', 'time', 'action', 'periodicity', 'is_published', 'lead_time', 'pleasant_habit')


class HabitCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Habit
        fields = ('user', 'place', 'time', 'action', 'periodicity', 'is_published', 'lead_time', 'pleasant_habit', '')


class HabitSerializer(serializers.ModelSerializer):
    pleasant_habit = PleasureHabitSerializer(source='habit', many=True)

    class Meta:
        model = Habit
        fields = '__all__'
