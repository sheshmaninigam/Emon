# Generated by Django 5.0.4 on 2024-05-01 07:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='addcar',
            name='cars_image',
            field=models.CharField(default='ABC', max_length=100),
        ),
    ]
