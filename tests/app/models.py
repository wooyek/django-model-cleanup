# coding=utf-8
from django.db import models

from django_model_cleanup.models import CleanMixin


class SomeModel(models.Model, CleanMixin):
    foo = models.CharField()
