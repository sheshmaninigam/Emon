# Generated by Django 5.0.4 on 2024-05-20 06:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0011_remove_transaction_user_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='date_time',
            field=models.CharField(default=0, max_length=100),
        ),
    ]
