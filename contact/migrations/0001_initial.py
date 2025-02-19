# Generated by Django 5.1.5 on 2025-02-14 09:42

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=254)),
                ('email', models.EmailField(max_length=254)),
                ('subject', models.CharField(choices=[('Order Inquiry', 'Order Inquiry'), ('Custom Art Requests', 'Custom Art Requests'), ('Product Availability', 'Product Availability'), ('Print Quality', 'Print Quality'), ('Returns and Exchanges', 'Returns and Exchanges'), ('Shipping and Delivery', 'Shipping and Delivery'), ('Collaboration and Partnerships', 'Collaboration and Partnerships'), ('Discounts', 'Discounts'), ('Shipping and Delivery', 'Shipping and Delivery'), ('Copyright and Usage Rights', 'Copyright and Usage Rights'), ('General Feedback', 'General Feedback')], max_length=254)),
                ('message', models.TextField(max_length=1024)),
                ('date_created', models.DateTimeField(default=django.utils.timezone.now)),
                ('responded', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name_plural': 'Contact Requests',
            },
        ),
    ]
