from sensor.serializers import EventSerializer, SensorSerializer
from sensor.models import Event, Sensor

from sensor.base_views import BaseCRUDAPIView


class EventAPIView(BaseCRUDAPIView):
    serializer_class = EventSerializer
    manager = Event.objects
    queryset = manager.all()

    def post(self, request):
        for sensor in request.data:
            pk_sensor = sensor['sensor_id']
            if not Sensor.objects.filter(pk=pk_sensor):
                Sensor.objects.create(pk=pk_sensor)
        return super(EventAPIView, self).post(request)


class SensorAPIView(BaseCRUDAPIView):
    serializer_class = SensorSerializer
    manager = Sensor.objects
    queryset = manager.all()