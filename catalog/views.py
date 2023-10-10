from django.contrib.auth.models import User
from django.db.models import F, Count, OuterRef, Sum
from rest_framework import viewsets, mixins
from rest_framework.permissions import IsAdminUser, IsAuthenticated

from catalog.models import Product, ProductAccess
from catalog.serializers import ProductStatisticsSerializer
from lessons.models import LessonInfo


class ProductStatisticsViewSet(viewsets.GenericViewSet, mixins.ListModelMixin):
    serializer_class = ProductStatisticsSerializer
    permission_classes = (IsAuthenticated, IsAdminUser)

    def get_queryset(self):
        total_active_users_count = User.objects.filter(
            is_active=True
        ).count()
        
        query_set = Product.objects.all().annotate(
            total_lessons_viewed=Count(
                LessonInfo.objects.filter(
                    lesson__product=OuterRef('id'),
                    viewed=True,
                ).values('id')
            ),
            total_time_spent_watching_lessons=Sum(
                LessonInfo.objects.filter(
                    lesson__product=OuterRef('id'),
                ).values('viewing_time_in_seconds')
            ),
            total_users_using_product=Count(
                ProductAccess.objects.filter(product=OuterRef('id')).values('id')
            ),
            purchase_percentage=F('total_users_using_product') /
                                float(total_active_users_count) * 100
        )
        
        return query_set
