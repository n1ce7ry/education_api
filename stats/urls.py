from rest_framework.routers import SimpleRouter
from stats.views import ProductStatsViewSet

router = SimpleRouter()

router.register('', ProductStatsViewSet, basename='stats')

urlpatterns = []

urlpatterns += router.urls
