# Generated by Django 2.2.1 on 2019-06-25 18:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('qlearning_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='map',
            name='path',
            field=models.CharField(max_length=119),
        ),
        migrations.AlterField(
            model_name='problem',
            name='map_related',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='qlearning_app.Map'),
        ),
    ]
