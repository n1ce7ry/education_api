from market.models import Lesson
from market.serializer import LessonSerializer
from rest_framework.viewsets import ReadOnlyModelViewSet


class LessonView(ReadOnlyModelViewSet):
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

# class LessonView(ModelViewSet):
#     
#     serializer_class = LessonSerializer
#     
#     def get_queryset(self):
#         user = self.request.user
#         
#         queryset = Lesson.objects.filter(
#             product__userproductrelation__user=user
#         ).prefetch_related('product')

        # annotated_lessons = lessons.annotate(
        #     viewed=Case(
        #         When(Q(userlessonrelation__user=user) | Q(userlessonrelation__lesson__in=lessons),
        #             # userlessonrelation__user=user, userlessonrelation__lesson__in=lessons,userlessonrelation__viewed=True,
        #              then=True),
        #         default=False,
        #         output_field=BooleanField()
        #     )
            # viewing_time=Sum('userlessonrelation__viewing_time_in_seconds')
            # viewing_time=F('userlessonrelation__viewing_time_in_seconds')
        # )

        # return annotated_lessons
