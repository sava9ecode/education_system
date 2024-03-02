from django.urls import path

from .views import LessonListAPIView, ProductListAPIView, StatisticListView

urlpatterns = [
    path('products/', ProductListAPIView.as_view(), name='products_list'),
    path(
        'product/<int:product_id>/lessons/',
        LessonListAPIView.as_view(),
        name='product_lessons',
    ),
    path('statistics/', StatisticListView.as_view(), name='statistics'),
]
