from django.db import models
from account.models import User
from product.models import Product


RATING_CHOICES = (
    (1, 1),
    (2, 2),
    (3, 3),
    (4, 4),
    (5, 5)
)


class Review(models.Model):
    author = models.ForeignKey(User,
                               on_delete=models.CASCADE,
                               related_name='author',
                               verbose_name='Author')
    product = models.ForeignKey(Product,
                                on_delete=models.CASCADE,
                                related_name='product',
                                verbose_name='Product')
    text = models.TextField()
    rating = models.IntegerField(choices=RATING_CHOICES)
