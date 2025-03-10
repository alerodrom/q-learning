# Generated by Django 2.2.1 on 2019-06-27 20:56

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('qlearning_app', '0004_auto_20190627_1855'),
    ]

    operations = [
        migrations.AlterField(
            model_name='problem',
            name='alpha',
            field=models.FloatField(default=0.1, validators=[django.core.validators.MinValueValidator(0.0), django.core.validators.MaxValueValidator(1.0)]),
        ),
        migrations.AlterField(
            model_name='problem',
            name='gamma',
            field=models.FloatField(default=0.9, validators=[django.core.validators.MinValueValidator(0.0), django.core.validators.MaxValueValidator(1.0)]),
        ),
    ]
