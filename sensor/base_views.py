from rest_framework.generics import GenericAPIView
from rest_framework.response import Response

from django.core.exceptions import ObjectDoesNotExist


class BaseCRUDAPIView(GenericAPIView):
    manager = None

    def get(self, request):
        return Response(self.serializer_class(self.manager.all(), many=True).data)

    def serialize(self, event):
        post_serializer = self.serializer_class(data=event)
        post_serializer.is_valid(raise_exception=True)
        post_serializer.save()

    def post(self, request):
        if type(request.data) is list:
            for event in request.data:
                self.serialize(event)
        else:
            self.serialize(request.data)
        return Response({'POST': 'success'})

    def put(self, request, pk):
        try:
            instance = self.manager.get(pk=pk)
        except ObjectDoesNotExist:
            return Response({'PUT': 'Error, object does not exists'})

        put_serializer = self.serializer_class(data=request.data, instance=instance)
        put_serializer.is_valid(raise_exception=True)
        put_serializer.save()
        return Response({'PUT': 'success'})

    def delete(self, request, pk):
        try:
            instance = self.manager.get(pk=pk)
        except ObjectDoesNotExist:
            return Response({'DELETE': 'Error, object does not exists'})

        instance.delete()
        return Response({'DELETE': f'success - del: {instance.name}'})