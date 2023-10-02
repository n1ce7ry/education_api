from rest_framework.serializers import ModelSerializer
from market.models import Lesson

        
class LessonSerializer(ModelSerializer):
    # viewing_time = serializers.IntegerField(source='userlessonrelation_set.first.viewing_time_in_seconds', default=0, read_only=True)
    # viewing_status = serializers.BooleanField(source='userlessonrelation_set.first.viewed', read_only=True) 
    # viewed = serializers.BooleanField()
    # viewing_time = serializers.IntegerField()
    
    # lesson_views = UserLessonRelationSerializer(many=True, read_only=True)
        
    class Meta:
        model = Lesson
        fields = ('title', 'video_link',
                  'duration_in_seconds',)
