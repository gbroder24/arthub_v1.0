from django.db import models

# Create your models here.


class Category(models.Model):

    class Meta:
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=254)
    display_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_display_name(self):
        return self.display_name


class Product(models.Model):
    category = models.ForeignKey(
        'Category',
        null=True,
        blank=True,
        on_delete=models.SET_NULL)
    sku = models.CharField(max_length=254, null=True, blank=True)
    artist = models.CharField(max_length=254)
    name = models.CharField(max_length=254)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    discount_percentage = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        default=0,  # Set default discount percentage to 0
        help_text="Discount percentage applied to the product price"
    )
    rating = models.DecimalField(
        max_digits=6,
        decimal_places=2,
        null=True,
        blank=True)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name
