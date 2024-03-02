from django.contrib.auth import get_user_model
from django.db.models import Count, F, FloatField
from django.db.models.functions import Cast
from django.shortcuts import get_object_or_404
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from .models import Lesson, Product, ProductAccess
from .serializers import (LessonSerializer, ProductSerializer,
                          StatisticSerializer)

User = get_user_model()


class ProductListAPIView(generics.ListAPIView):
    queryset = Product.objects.annotate(count_lessons=Count('lessons')).filter(
        is_active=True
    )
    serializer_class = ProductSerializer


class LessonListAPIView(generics.ListAPIView):
    serializer_class = LessonSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        product_id = self.kwargs.get('product_id')
        get_object_or_404(
            ProductAccess.objects.filter(
                user=self.request.user, product_id=product_id
            )
        )
        return Lesson.objects.filter(product__id=product_id)


class StatisticListView(generics.ListAPIView):
    def get_queryset(self):
        queryset = Product.objects.annotate(
            total_students=Count('group__students'),
            fullness_percent=Cast(
                100.0 * Count('group__students') / F('max_students'),
                FloatField(),
            ),
            access_percent=Cast(
                100.0
                * Count(ProductAccess.objects.filter().count())
                / User.objects.count(),
                FloatField(),
            ),
        )
        return queryset

    serializer_class = StatisticSerializer
    permission_classes = [IsAuthenticated]
