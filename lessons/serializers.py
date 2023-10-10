from rest_framework import serializers

from lessons.models import Lesson


class LessonsSerializer(serializers.ModelSerializer):
    viewing_time = serializers.IntegerField()
    viewed = serializers.BooleanField()

    
    class Meta:
        model = Lesson
        fields = ('title', 'viewing_time', 'viewed')


class LessonByProductSerializer(LessonsSerializer):
    pass
