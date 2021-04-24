from rest_framework import serializers
from AdjustHomeTask.api.models import DatasetModel


class DatasetModelSerializer(serializers.ModelSerializer):
    date = serializers.DateField(required=False)
    channel = serializers.CharField(required=False)
    country = serializers.CharField(required=False)
    os = serializers.CharField(required=False)
    impressions = serializers.IntegerField(required=False)
    clicks = serializers.IntegerField(required=False)
    installs = serializers.IntegerField(required=False)
    spend = serializers.FloatField()
    revenue = serializers.FloatField()
    cpi = serializers.FloatField()

    class Meta:
        model = DatasetModel
        fields = '__all__'

