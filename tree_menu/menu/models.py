from django.db import models
from django.db.models import Q


class Menu(models.Model):
    name = models.CharField(max_length=64)
    parent = models.ForeignKey(
        'self',
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        related_name='up_menu'
    )

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = 'Menu'
        verbose_name_plural = 'Menus'
        constraints = (
            models.constraints.UniqueConstraint(
                fields=('name',),
                condition=Q(parent__isnull=True),
                name='unique_null_parent_',
            ),
            models.constraints.UniqueConstraint(
                fields=('name', 'parent'),
                name='unique_parent',
            ),
        )
