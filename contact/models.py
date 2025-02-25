from django.db import models
from django.utils import timezone

# Create your models here.


class Contact(models.Model):
    class Meta:
        verbose_name_plural = 'Contact Requests'

    SUBJECTS = (
        ('Order Inquiry', 'Order Inquiry'),
        ('Custom Art Requests', 'Custom Art Requests'),
        ('Product Availability', 'Product Availability'),
        ('Print Quality', 'Print Quality'),
        ('Returns and Exchanges', "Returns and Exchanges"),
        ('Shipping and Delivery', "Shipping and Delivery"),
        ('Collaboration and Partnerships', "Collaboration and Partnerships"),
        ('Discounts', "Discounts"),
        ('Shipping and Delivery', "Shipping and Delivery"),
        ('Copyright and Usage Rights', "Copyright and Usage Rights"),
        ('General Feedback', "General Feedback"),
    )

    name = models.CharField(max_length=254)
    email = models.EmailField()
    subject = models.CharField(choices=SUBJECTS, max_length=254,)
    message = models.TextField(max_length=1024)
    date_created = models.DateTimeField(default=timezone.now)
    responded = models.BooleanField(default=False)

    def __str__(self):
        return self.email
