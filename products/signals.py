from django.db import transaction
from django.db.models.signals import post_delete, post_save
from django.dispatch import receiver
from django.shortcuts import get_list_or_404

from .models import Group, ProductAccess


def get_groups_assosiated_with_product(product):
    return get_list_or_404(
        Group.objects.prefetch_related('students'), product=product
    )


@receiver(post_save, sender=ProductAccess)
def distribute_students_equally(sender, instance, created, **kwargs):
    if created:
        product = instance.product

        with transaction.atomic():
            groups = get_groups_assosiated_with_product(product)
            total_students = sum(group.students.count() for group in groups)

            FLAG = False
            if all(
                [
                    group.students.count() >= product.min_students
                    for group in groups
                ]
            ):
                FLAG = True

            groups = sorted(
                groups,
                key=lambda group: group.students.count(),
                reverse=True if not FLAG else False,
            )

            if total_students < product.max_students:
                if not FLAG:
                    for group in groups:
                        if group.students.count() < product.min_students:
                            group.students.add(instance.user)
                            break
                else:
                    groups[0].students.add(instance.user)
            else:
                instance.delete()


@receiver(post_delete, sender=ProductAccess)
def delete_user_from_count_group(sender, instance, **kwargs):
    groups = get_groups_assosiated_with_product(instance.product)
    for group in groups:
        group.students.remove(instance.user)
