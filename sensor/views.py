from drf_yasg.utils import swagger_auto_schema
from rest_framework.decorators import api_view
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from sensor.base_views import CRBaseAPIView, UDBaseIView
from sensor.models import Event, Sensor
from sensor.service import EventMixin, SensorMixin


class CREventAPIView(EventMixin, CRBaseAPIView):
    manager = Event.objects
    queryset = manager.all()
    permission_classes = (AllowAny, )

    @swagger_auto_schema(operation_description='output of all events (list)')
    def get(self, request):
        page = self.paginate_queryset(self.get_queryset())
        if page:
            return self.get_paginated_response(self.get_serializer(page, many=True).data)
        return super(CREventAPIView, self).get(request)

    @swagger_auto_schema(operation_description='allows you to add a list or one event to the database to the db')
    def post(self, request):
        pk_sensor = None
        if type(request.data) is dict:
            pk_sensor = request.data['sensor_id']
        else:
            for sensor in request.data:
                pk_sensor = sensor['sensor_id']
        if not Sensor.objects.filter(pk=pk_sensor):
            Sensor.objects.create(pk=pk_sensor)
        return super(CREventAPIView, self).post(request)


class UPEventAPIView(EventMixin, UDBaseIView):

    manager = Event.objects
    queryset = manager.all()
    permission_classes = (AllowAny, )

    @swagger_auto_schema(operation_description='allows to change event data, accepts event id')
    def put(self, request, pk):
        return super(UPEventAPIView, self).put(request, pk)

    @swagger_auto_schema(operation_description='removes event data from the database, accepts the event id')
    def delete(self, request, pk):
        return super(UPEventAPIView, self).delete(request, pk)


class CRSensorAPIView(SensorMixin, CRBaseAPIView):

    @swagger_auto_schema(operation_description='output of all sensors (list)')
    def get(self, request):
        return super(CRSensorAPIView, self).get(request)

    @swagger_auto_schema('allows you to add a list or one sensor to the database to the db')
    def post(self, request):
        return super(CRSensorAPIView, self).post(request)


class UPSensorAPIView(SensorMixin, UDBaseIView):

    @swagger_auto_schema(operation_description='allows to change sensor data, accepts sensor id')
    def put(self, request, pk):
        return super(UPSensorAPIView, self).put(request, pk)

    @swagger_auto_schema(operation_description='removes sensor data from the database, accepts the sensor id')
    def delete(self, request, pk):
        return super(UPSensorAPIView, self).delete(request, pk)


class SensorAllEventsAPIView(EventMixin, GenericAPIView):

    @swagger_auto_schema(operation_description='returns all events associated with sensor, accepts the sensor id')
    def get(self, request, pk):
        self.queryset = self.filter_queryset(Event.objects.filter(sensor_id=pk))
        if self.get_queryset():
            page = self.paginate_queryset(self.get_queryset())
            if page:
                return self.get_paginated_response(self.get_serializer(page, many=True).data)
            return Response(self.get_serializer(self.get_queryset(), many=True).data)
        return Response({'GET': 'Error, events does not exists'})