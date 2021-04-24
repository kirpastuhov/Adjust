from django.db.models import Sum

from AdjustHomeTask.api.models import DatasetModel


def sort_queryset(queryset, sort_params):
    fields = [field.name for field in DatasetModel._meta.get_fields()]
    if sort_params:
        sort = [x.strip() for x in sort_params.split(",") if x.strip().replace("-", "") in fields]
        if len(sort) > 0:
            queryset = queryset.order_by(*sort)

    return queryset


def group_queryset(queryset, group_params):
    if group_params is not None:
        fields = ["date", "channel", "country", "os"]
        group_by = [x.strip() for x in group_params.split(",") if x.strip() in fields]
        if len(group_by) > 0:
            aggregated_fields = ['impressions', 'clicks', 'installs', 'spend', 'revenue', 'cpi']
            annotated_fields = {af: Sum(af) for af in aggregated_fields}
            queryset = queryset.values(*group_by).annotate(**annotated_fields)
    return queryset
