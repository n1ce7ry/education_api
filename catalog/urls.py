from django.urls import path

from catalog.views import ProductStatisticsViewSet


urlpatterns = [
    path('statistics/', ProductStatisticsViewSet.as_view({'get': 'list'}))
]
