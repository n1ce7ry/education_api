from django.urls import path, include
from rest_framework.routers import SimpleRouter
from lessons.views import LessonsByProductViewSet, LessonsListViewSet

router = SimpleRouter()

router.register('', LessonsListViewSet, 'lessons')

urlpatterns = [
    path('', include(router.urls)),
    path('by-product/<int:product_id>',
         LessonsByProductViewSet.as_view({'get': 'list'})),
]
