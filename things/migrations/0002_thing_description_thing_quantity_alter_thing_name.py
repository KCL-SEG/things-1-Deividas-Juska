# Generated by Django 4.2.5 on 2023-10-16 15:20

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('things', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='thing',
            name='description',
            field=models.CharField(blank=True, max_length=120),
        ),
        migrations.AddField(
            model_name='thing',
            name='quantity',
            field=models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(100), django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AlterField(
            model_name='thing',
            name='name',
            field=models.CharField(max_length=30, unique=True),
        ),
    ]
