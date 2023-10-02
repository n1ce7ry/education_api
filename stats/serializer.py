from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from market.models import Product

        
class ProductSerializer(ModelSerializer):
    lessons_viewed = serializers.IntegerField(read_only=True)
    spend_time_watching_lessons = serializers.IntegerField(read_only=True)
    number_of_students_attending_course = serializers.IntegerField(read_only=True)
    percentage_of_product_purchase = serializers.FloatField(read_only=True)
        
    class Meta:
        model = Product
        fields = ('owner', 'name',
                  'lessons_viewed',
                  'spend_time_watching_lessons',
                  'number_of_students_attending_course',
                  'percentage_of_product_purchase',)
