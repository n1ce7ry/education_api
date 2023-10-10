from rest_framework import serializers


class ProductStatisticsSerializer(serializers.Serializer):
    name = serializers.CharField()
    total_lessons_viewed = serializers.IntegerField()
    total_time_spent_watching_lessons = serializers.IntegerField()
    total_users_using_product = serializers.IntegerField()
    purchase_percentage = serializers.FloatField()
