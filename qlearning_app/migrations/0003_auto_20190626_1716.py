# Generated by Django 2.2.1 on 2019-06-26 17:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('qlearning_app', '0002_auto_20190625_1802'),
    ]

    operations = [
        migrations.AddField(
            model_name='map',
            name='name',
            field=models.CharField(default='MAPPPP', max_length=120),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='result',
            name='maps',
            field=models.CharField(max_length=100000),
        ),
    ]
