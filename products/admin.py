from django.contrib import admin

from .models import Group, Lesson, Product, ProductAccess


class LessonInline(admin.StackedInline):
    model = Lesson
    extra = 0


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    model = Product
    inlines = (LessonInline,)
    list_display = (
        'name',
        'author',
        'price',
        'start_datetime',
        'min_students',
        'max_students',
        'is_active',
    )
    list_editable = (
        'price',
        'min_students',
        'max_students',
        'is_active',
    )


@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    model = Lesson
    list_display = (
        'name',
        'video_link',
        'product',
    )


@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    model = Group
    list_display = (
        'name',
        'product',
    )


@admin.register(ProductAccess)
class ProductAccessAdmin(admin.ModelAdmin):
    model = ProductAccess
    list_display = (
        'user',
        'product',
        'granted_at',
    )
