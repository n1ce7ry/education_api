from django.contrib import admin

from lessons.models import Lesson, LessonInfo


@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    pass

    
@admin.register(LessonInfo)
class LessonInfoAdmin(admin.ModelAdmin):
    pass
