from django.contrib.auth.models import User
from django.db import models


class Product(models.Model):
    owner = models.ForeignKey(User, on_delete=models.PROTECT)
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class ProductAccess(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name='accesses'
    )
    access = models.BooleanField(default=True)

    def __str__(self):
        return (
            f'{self.user} '
            f'{"has access to the" if self.access is True else "doesn’t have access to the"} '
            f'{self.product}'
        )
