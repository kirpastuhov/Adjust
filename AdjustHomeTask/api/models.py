from django.db import models
from computedfields.models import ComputedFieldsModel, computed


class DatasetModel(ComputedFieldsModel):
    date = models.DateField(blank=False)
    channel = models.CharField(max_length=255)
    country = models.CharField(max_length=2)
    os = models.CharField(max_length=7)
    impressions = models.IntegerField()
    clicks = models.IntegerField()
    installs = models.IntegerField()
    spend = models.FloatField()
    revenue = models.FloatField()

    @computed(models.FloatField(null=True), depends=[['self', ['spend', 'installs']]])
    def cpi(self):
        return float(self.spend) / float(self.installs)
