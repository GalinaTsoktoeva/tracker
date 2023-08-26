from django.contrib import admin

from habit.models import Habit


@admin.register(Habit)
class HabitAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'place', 'time', 'action', 'periodicity', 'is_published', 'lead_time', 'pleasant_habit', 'is_pleasant_habit', 'reward',)
