from django.contrib.auth.models import User
from django.core.validators import (
    MinValueValidator,
    MinLengthValidator,
    MaxValueValidator,
)
from django.core.validators import RegexValidator
from django.db import models
from django.db.models import Avg
from django.contrib.postgres.fields import ArrayField


class TimeStampedModel(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Map(TimeStampedModel):
    path = models.CharField(max_length=119)
    pos_init_x = models.IntegerField()
    pos_init_y = models.IntegerField()
    pos_end_x = models.IntegerField()
    pos_end_y = models.IntegerField()

    class Meta:
        verbose_name = "map"
        verbose_name_plural = "maps"

    def get_map(self):
        return self.path

    def height(self):
        return 6

    def width(self):
        return 6


class Problem(TimeStampedModel):
    map_related = models.OneToOneField(Map, on_delete=models.CASCADE)
    np_zeros = models.BooleanField(default=True)
    epochs = models.IntegerField(default=50)
    gamma = models.FloatField(default=0.9)
    alpha = models.FloatField(default=0.1)

    class Meta:
        verbose_name = "problem"
        verbose_name_plural = "problems"


class Result(TimeStampedModel):
    problem = models.OneToOneField(Problem, on_delete=models.CASCADE)
    maps = models.CharField(max_length=10000)
    steps = models.IntegerField()
    reward = models.FloatField()
    path = models.CharField(max_length=10000)

    class Meta:
        verbose_name = "result"
        verbose_name_plural = "results"
