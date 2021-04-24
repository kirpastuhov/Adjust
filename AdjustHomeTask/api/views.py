from rest_framework import viewsets
from django_filters import rest_framework as rest_framework_filters

from AdjustHomeTask.api.models import DatasetModel
from AdjustHomeTask.api.serializers import DatasetModelSerializer
from AdjustHomeTask.api.utils import sort_queryset, group_queryset


class DatasetFilter(rest_framework_filters.FilterSet):
    date = rest_framework_filters.DateFromToRangeFilter()

    class Meta:
        model = DatasetModel
        fields = ('date', 'channel', 'country', 'os')


class DatasetViewSet(viewsets.ModelViewSet):
    queryset = DatasetModel.objects.all()
    serializer_class = DatasetModelSerializer
    filterset_class = DatasetFilter

    def get_queryset(self):
        queryset = self.queryset
        group_by = self.request.query_params.get("group_by")
        sort_by = self.request.query_params.get("sort_by")

        queryset = sort_queryset(queryset, sort_by)
        queryset = group_queryset(queryset, group_by)

        return queryset
