# Generated by Django 2.2.1 on 2019-06-24 18:58

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Map",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("created", models.DateTimeField(auto_now_add=True)),
                ("modified", models.DateTimeField(auto_now=True)),
                ("path", models.CharField(max_length=120)),
                ("pos_init_x", models.IntegerField()),
                ("pos_init_y", models.IntegerField()),
                ("pos_end_x", models.IntegerField()),
                ("pos_end_y", models.IntegerField()),
            ],
            options={"verbose_name": "map", "verbose_name_plural": "maps"},
        ),
        migrations.CreateModel(
            name="Problem",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("created", models.DateTimeField(auto_now_add=True)),
                ("modified", models.DateTimeField(auto_now=True)),
                ("np_zeros", models.BooleanField(default=True)),
                ("epochs", models.IntegerField(default=50)),
                ("gamma", models.FloatField(default=0.9)),
                ("alpha", models.FloatField(default=0.1)),
                (
                    "map_related",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="qlearning_app.Map",
                    ),
                ),
            ],
            options={"verbose_name": "problem", "verbose_name_plural": "problems"},
        ),
        migrations.CreateModel(
            name="Result",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("created", models.DateTimeField(auto_now_add=True)),
                ("modified", models.DateTimeField(auto_now=True)),
                ("maps", models.CharField(max_length=10000)),
                ("steps", models.IntegerField()),
                ("reward", models.FloatField()),
                ("path", models.CharField(max_length=10000)),
                (
                    "problem",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="qlearning_app.Problem",
                    ),
                ),
            ],
            options={"verbose_name": "result", "verbose_name_plural": "results"},
        ),
    ]
