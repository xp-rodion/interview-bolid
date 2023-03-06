import django_filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.pagination import PageNumberPagination

from sensor.models import Event
from sensor.serializers import EventSerializer


class BasePaginationClass(PageNumberPagination):
    page_size = 5
    page_query_param = 'page_size'
    max_page_size = 50


class EventFilter(django_filters.FilterSet):
    temperature = django_filters.NumberFilter()
    humidity = django_filters.NumberFilter()

    class Meta:
        model = Event
        fields = ('temperature', 'humidity', )


class EventMixin:
    pagination_class = BasePaginationClass
    filter_backends = [DjangoFilterBackend]
    filterset_class = EventFilter
    serializer_class = EventSerializer