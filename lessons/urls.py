from rest_framework.routers import SimpleRouter
from lessons.views import LessonsListViewSet

router = SimpleRouter()

router.register('', LessonsListViewSet, 'lessons')

urlpatterns = []

urlpatterns += router.urls
