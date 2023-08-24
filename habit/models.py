from datetime import datetime

from django.db import models

from users.models import User

NULLABLE = {
    'null': True,
    'blank': True
}


class Habit(models.Model):

    """ класс описывает Атомные привычки """

    TITLE_PERIODICITY = [
        (1, 'ежедневная'),
        (2, 'еженедельная'),
        (3, 'eжемесячная')
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='пользователь', **NULLABLE)
    place = models.CharField(max_length=150, verbose_name='место')
    time = models.DateTimeField(default=datetime.now(), verbose_name='время')
    action = models.CharField(max_length=150, verbose_name='действие')
    is_pleasant_habit = models.BooleanField(default=False, verbose_name='приятная привычка', **NULLABLE)
    is_related_habit = models.BooleanField(default=False, verbose_name='связанная привычка', **NULLABLE)
    periodicity = models.PositiveSmallIntegerField(verbose_name='периодичность', default=1, choices=TITLE_PERIODICITY)
    reward = models.TextField(verbose_name='вознаграждение', **NULLABLE)
    lead_time = models.TimeField(verbose_name='время выполнения', )
    is_published = models.BooleanField(default=False, verbose_name='признак публичности')

    def __str__(self):
        return f"я буду {self.action} в {self.time} в {self.place}"

    class Meta:
        verbose_name = 'привычка'
        verbose_name_plural = 'привычки'