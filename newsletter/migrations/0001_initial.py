# Generated by Django 5.1.5 on 2025-02-17 15:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Email',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(error_messages={'unique': 'This email is already subscribed.'}, max_length=254, unique=True)),
            ],
            options={
                'verbose_name_plural': 'Email Addresses',
            },
        ),
    ]
