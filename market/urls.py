from rest_framework.routers import SimpleRouter
from market.views import LessonView

router = SimpleRouter()

router.register('lessons', LessonView, basename='Lesson')

urlpatterns = []

urlpatterns += router.urls
