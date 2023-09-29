from django.contrib import admin
from market.models import (
    Product,
    Lesson,
    UserProductRelation,
    UserLessonRelation,
)


admin.site.register(Product)
admin.site.register(Lesson)
admin.site.register(UserProductRelation)
admin.site.register(UserLessonRelation)
