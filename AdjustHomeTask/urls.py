from django.urls import include, path
from rest_framework import routers
from AdjustHomeTask.api.views import DatasetViewSet

router = routers.DefaultRouter()
router.register(r'dataset', DatasetViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
