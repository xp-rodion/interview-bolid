from django.contrib import admin

from sensor.models import Event, Sensor

admin.site.register(Event)
admin.site.register(Sensor)