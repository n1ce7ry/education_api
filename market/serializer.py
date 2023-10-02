from rest_framework.serializers import ModelSerializer
from market.models import Lesson

        
class LessonSerializer(ModelSerializer):
    
    class Meta:
        model = Lesson
        fields = ('title', 'video_link',
                  'duration_in_seconds',)
