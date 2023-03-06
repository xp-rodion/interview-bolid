from rest_framework.generics import GenericAPIView
from rest_framework.response import Response

from sensor.serializers import SensorSerializer
from sensor.models import Event, Sensor
from sensor.base_views import BaseCRUDAPIView
from sensor.service import EventMixin


class EventAPIView(EventMixin, BaseCRUDAPIView):
    manager = Event.objects
    queryset = manager.all()

    def get_queryset(self):
        return self.filter_queryset(super(EventAPIView, self).get_queryset())

    def get(self, request):
        page = self.paginate_queryset(self.get_queryset())
        if page:
            return self.get_paginated_response(self.get_serializer(page, many=True).data)
        return super(EventAPIView, self).get(request)

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


class SensorAllEventsAPIView(EventMixin, GenericAPIView):

    def get(self, request, pk):
        self.queryset = self.filter_queryset(Event.objects.filter(sensor_id=pk))
        if self.get_queryset():
            page = self.paginate_queryset(self.get_queryset())
            if page:
                return self.get_paginated_response(self.get_serializer(page, many=True).data)
            return Response(self.get_serializer(self.get_queryset(), many=True).data)
        return Response({'GET': 'Error, objects  does not exists'})