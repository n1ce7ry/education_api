from django.db.models import F, Count, Case, Sum, When
from rest_framework.viewsets import ReadOnlyModelViewSet
from market.models import Product
from stats.serializer import ProductSerializer


class ProductStatsViewSet(ReadOnlyModelViewSet):
    serializer_class = ProductSerializer
    
    def get_queryset(self):
        user = self.request.user
        
        if user.is_authenticated:

            queryset = Product.objects.all().annotate(
                lessons_viewed=Count(
                    Case(
                        When(userproductrelation__user__userlessonrelation__viewed=True, then=1)
                    )
                ),
                spend_time_watching_lessons=Sum(
                    F("userproductrelation__user__userlessonrelation__viewing_time_in_seconds")
                ),
                number_of_students_attending_course=Count(
                    Case(
                        When(userproductrelation__access=True, then=1)
                    )
                ),
                percentage_of_product_purchase=Count(
                    Case(
                        When(userproductrelation__access=True, then=1)
                    )
                ) /
                Count(
                    F('userproductrelation__user')
                ),
            )
            
            return queryset
        else:
            return None
