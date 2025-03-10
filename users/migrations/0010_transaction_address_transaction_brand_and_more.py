# Generated by Django 5.0.4 on 2024-05-20 05:57

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0009_transaction_user_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='transaction',
            name='address',
            field=models.CharField(default='abc', max_length=300),
        ),
        migrations.AddField(
            model_name='transaction',
            name='brand',
            field=models.CharField(default='abc', max_length=100),
        ),
        migrations.AddField(
            model_name='transaction',
            name='city',
            field=models.CharField(default='abc', max_length=100),
        ),
        migrations.AddField(
            model_name='transaction',
            name='date_time',
            field=models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AddField(
            model_name='transaction',
            name='model',
            field=models.CharField(default='abc', max_length=100),
        ),
        migrations.AddField(
            model_name='transaction',
            name='name',
            field=models.CharField(default='abc', max_length=100),
        ),
        migrations.AddField(
            model_name='transaction',
            name='postal_code',
            field=models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(100)]),
        ),
        migrations.AddField(
            model_name='transaction',
            name='price',
            field=models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AddField(
            model_name='transaction',
            name='state',
            field=models.CharField(default='abc', max_length=100),
        ),
    ]
