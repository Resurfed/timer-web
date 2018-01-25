from rest_framework.response import Response


class TimeRetrieveModelMixin(object):

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.rank = instance.actual_rank()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)


class TimeListModelMixin(object):

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        page = self.paginate_queryset(queryset)
        if page is not None:
            for instance in page:
                instance.rank = instance.actual_rank()

            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
