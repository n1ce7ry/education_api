from django.db.models import F, Q, FilteredRelation
from rest_framework import viewsets, mixins
from rest_framework.permissions import IsAuthenticated

from catalog.models import ProductAccess
from lessons.models import Lesson
from lessons.serializers import LessonsSerializer


class LessonsListViewSet(viewsets.GenericViewSet, mixins.ListModelMixin):
    serializer_class = LessonsSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        user = self.request.user
        
        accesses = ProductAccess.objects.filter(
            user=user,
            access=True,
        )

        query_set = Lesson.objects.filter(
            product__in=accesses.values('product_id')
        ).alias(
            view_info=FilteredRelation(
                'views',
                condition=Q(views__user=user),
            )
        ).annotate(
            viewing_time=F('view_info__viewing_time_in_seconds'),
            viewed=F('view_info__viewed'),
        )
        
        return query_set
