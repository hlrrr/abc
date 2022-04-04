from pyexpat import model
from django.db import models
from django_countries.fields import CountryField
from core import models as core_models
from users import models as user_models
# Create your models here.


class Room(core_models.TimeStampedModel):

    """ Room Model Definition """

    name = models.CharField(max_length=140)
    description = models.TextField()
    country = CountryField()
    city = models. CharField(max_length=100)
    price = models.IntegerField()
    address = models.CharField(max_length=140)
    beds = models.IntegerField()
    bath = models.IntegerField()
    guests = models.IntegerField()
    check_in = models.TimeField()
    check_out = models.TimeField()
    instant_book = models. BooleanField(default=False)
# one top many (user to rooms)
    host = models.ForeignKey(user_models.User, on_delete=models.CASCADE)

# name값을 Rooom 이름으로 표출
    def __str__(self):
        return self.name
