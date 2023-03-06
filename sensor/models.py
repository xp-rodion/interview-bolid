from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


class Sensor(models.Model):
    name = models.CharField(max_length=128, verbose_name='Имя датчика', blank=True, null=True, default=None)
    type = models.IntegerField(verbose_name='Тип датчика', validators=[MinValueValidator(1), MaxValueValidator(3)], blank=True, null=True, default=None)

    def __str__(self):
        return f'ID - {str(self.pk)}'


class Event(models.Model):
    sensor_id = models.ForeignKey(to=Sensor, verbose_name='ID датчика', on_delete=models.PROTECT, db_column='sensor_id')
    name = models.CharField(max_length=128, verbose_name='Имя события')
    temperature = models.IntegerField(verbose_name='Температура', blank=True, null=True, default=None)
    humidity = models.IntegerField(verbose_name='Влажность', blank=True, null=True, default=None)

    def __str__(self):
        return f'ID - {str(self.pk)}'