from django.urls import reverse
from django.db import models


class Category(models.Model):
    name = models.CharField( max_length=200,
                             db_index=True )
    slug = models.SlugField( max_length=200,
                             db_index=True,
                             unique=True )

    class Meta:
        ordering = ('name',)
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse( 'shop:product_list_by_category',
                        args=[self.slug] )

class Product(models.Model):
    category = models.ForeignKey( Category,
                                  related_name='products',
                                  on_delete=models.CASCADE
                                  )
    name = models.CharField( max_length=200, db_index=True )
    slug = models.SlugField( max_length=200, db_index=True )
    image = models.ImageField( upload_to='products',
                               blank=True )
    description = models.TextField( blank=True )
    price = models.DecimalField( max_digits=10, decimal_places=2 )
    stock = models.PositiveIntegerField()
    available = models.BooleanField( default=True )
    created = models.DateTimeField( auto_now_add=True )
    updated = models.DateTimeField( auto_now=True )

    class Meta:
        ordering = ('name',)
        index_together = (('id', 'slug'),)


    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse( 'shop:product_detail',
                        args=[self.id, self.slug] )

# class Choice(models.Model):
#     DoesNotExist = None
#     question = models.ForeignKey(Question, on_delete=models.CASCADE)
#     choice_text = models.CharField(max_length=200)
#     votes = models.IntegerField(default=0)
#
#     def __str__(self):
#         return self.choice_text