from django.db import models

# Create your models here.


class TimeStampedModel(models.Model):

    """ Time Stamped Model """

    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)

# DB에 반영되지 않도록 설정

    class Meta:
        abstract = True
