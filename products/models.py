from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

User = get_user_model()


def validate_positive(value):
    if value < 0:
        raise ValidationError('Цена не может быть отрицательной')


class Product(models.Model):
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, verbose_name='Автор'
    )
    name = models.CharField('Название', max_length=255)
    start_datetime = models.DateTimeField('Дата и время начала')
    price = models.DecimalField(
        'Цена', max_digits=10, decimal_places=2, validators=[validate_positive]
    )
    min_students = models.IntegerField(
        'Минимальное количество студентов',
        default=0,
        validators=[MinValueValidator(0)],
    )
    max_students = models.IntegerField(
        'Максимальное количество студентов',
        default=10,
        validators=[MaxValueValidator(10)],
    )
    is_active = models.BooleanField('Доступен для покупки', default=True)

    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'Продукты'

    def __str__(self):
        return self.name


class Lesson(models.Model):
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        verbose_name='Продукт',
        related_name='lessons',
    )
    name = models.CharField('Название', max_length=255)
    video_link = models.URLField('Ссылка на урок', unique=True)

    class Meta:
        verbose_name = 'урок'
        verbose_name_plural = 'Уроки'

    def __str__(self):
        return self.name


class ProductAccess(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, verbose_name='Студент'
    )
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, verbose_name='Продукт'
    )
    granted_at = models.DateTimeField(
        'Дата и время получения доступа', auto_now_add=True
    )

    class Meta:
        verbose_name = 'доступ к продукту'
        verbose_name_plural = 'Доступы к продукту'

    def __str__(self):
        return (
            f'{self.user} имеет доступ к продукту '
            f'{self.product} с {self.granted_at}'
        )


class Group(models.Model):
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, verbose_name='Продукт'
    )
    name = models.CharField('Название', max_length=255)
    students = models.ManyToManyField(User, blank=True)

    class Meta:
        verbose_name = 'группа'
        verbose_name_plural = 'Группы'

    def __str__(self):
        return self.name
