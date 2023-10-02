from market.models import Lesson
from market.serializer import LessonSerializer
from rest_framework.viewsets import ReadOnlyModelViewSet


class LessonViewSet(ReadOnlyModelViewSet):
    serializer_class = LessonSerializer
    
    def get_queryset(self):
        user = self.request.user
        
        if user.is_authenticated:

            queryset = Lesson.objects.filter(
                product__userproductrelation__user=user
            ).prefetch_related('product')
            
            return queryset
        else:
            return None
