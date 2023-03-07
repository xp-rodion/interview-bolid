from django.contrib import admin

from sensor.models import Event, Sensor


@admin.register(Event)
class EventAdminModel(admin.ModelAdmin):
    fields = ('sensor_id', 'name', 'temperature', 'humidity')
    list_display = ('name', )


@admin.register(Sensor)
class SensorAdminModel(admin.ModelAdmin):
    fields = ('name', 'type')
    list_display = ('name', )