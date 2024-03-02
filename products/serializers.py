from django.contrib.auth import get_user_model
from rest_framework import serializers

from .models import Lesson, Product

User = get_user_model()


class ProductSerializer(serializers.ModelSerializer):
    count_lessons = serializers.IntegerField()

    class Meta:
        model = Product
        fields = (
            'author',
            'name',
            'start_datetime',
            'price',
            'count_lessons',
        )


class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = ('name', 'video_link')


class StatisticSerializer(serializers.ModelSerializer):
    students_count = serializers.IntegerField(source='total_students')
    group_fullness = serializers.FloatField(source='fullness_percent')
    product_percent = serializers.FloatField(source='access_percent')

    class Meta:
        model = Product
        fields = (
            'name',
            'students_count',
            'group_fullness',
            'product_percent',
        )
