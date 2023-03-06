from rest_framework import serializers

from sensor.models import Event, Sensor


class EventSerializer(serializers.ModelSerializer):

    class Meta:
        model = Event
        fields = ('sensor_id', 'name', 'temperature', 'humidity')

    def create(self, validated_data):
        return Event.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.sensor_id = validated_data.get('sensor_id', instance.sensor_id)
        instance.name = validated_data.get('name', instance.name)
        instance.temperature = validated_data.get('temperature', instance.temperature)
        instance.humidity = validated_data.get('humidity', instance.humidity)
        instance.save()
        return instance


class SensorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Sensor
        fields = ('pk', 'name', 'type')

    def create(self, validated_data):
        return Sensor.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.type = validated_data.get('type', instance.type)
        instance.save()
        return instance

