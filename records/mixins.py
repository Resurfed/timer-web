from rest_framework.response import Response


class TimeRetrieveModelMixin(object):

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.rank = instance.actual_rank()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)
