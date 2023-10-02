from rest_framework.routers import SimpleRouter
from market.views import LessonViewSet

router = SimpleRouter()

router.register('lessons', LessonViewSet, basename='Lessons')

urlpatterns = []

urlpatterns += router.urls
