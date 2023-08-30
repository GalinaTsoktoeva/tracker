from datetime import datetime

from celery import shared_task
from django.conf import settings
from telebot import TeleBot
from habit.models import Habit


@shared_task
def habits_notification():
    #print("start")
    habits = Habit.objects.all()
    for habit in habits:
        if habit.time == datetime.now():
            bot = TeleBot(settings.API_TELEGRAM)
            message = f"Трекер привычек напоминает: требуется совершить {habit.action} в {habit.place} в {habit.time}"
            bot.send_message(habit.user.chat_id, message)
    #print("end")