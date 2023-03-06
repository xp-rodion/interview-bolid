from rest_framework.generics import GenericAPIView
from rest_framework.response import Response

from sensor.serializers import EventSerializer, SensorSerializer
from sensor.models import Event, Sensor
from sensor.base_views import BaseCRUDAPIView
from sensor.paginate import BasePaginationClass


class EventAPIView(BaseCRUDAPIView):
    serializer_class = EventSerializer
    manager = Event.objects
    queryset = manager.all()
    pagination_class = BasePaginationClass

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


class SensorAllEventsAPIView(GenericAPIView):
    pagination_class = BasePaginationClass
    serializer_class = EventSerializer
    queryset = None

    def get(self, request, pk):
        self.queryset = Event.objects.filter(sensor_id=pk)
        if self.get_queryset():
            page = self.paginate_queryset(self.get_queryset())
            if page:
                return self.get_paginated_response(self.get_serializer(page, many=True).data)
            return Response(self.get_serializer(self.get_queryset(), many=True).data)
        return Response({'GET': 'Error, objects  does not exists'})