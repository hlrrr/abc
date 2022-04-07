from django.db import models
from django_countries.fields import CountryField
from core import models as core_models
from users import models as user_models

# Create your models here.


class AbstractItem(core_models.TimeStampedModel):
    """AbstractItem"""

    name = models.CharField(max_length=50)

    class Meta:
        abstract = True

    def __str__(self):
        return self.name


class RoomType(AbstractItem):
    """RoomType Model Def."""

    # admin 메뉴명 변경
    class Meta:
        verbose_name = "Room Type"
        # ordering = ["updated"]


class Amenity(AbstractItem):
    """Amenity Model Def."""

    # admin 메뉴명 변경
    class Meta:
        verbose_name_plural = "Amenities"


class Facility(AbstractItem):
    """Facility Model Def."""

    # admin 메뉴명 변경
    class Meta:
        verbose_name_plural = "Facilities"


class HouseRule(AbstractItem):
    """HouseRule Model Def."""

    # admin 메뉴명 변경
    class Meta:
        verbose_name = "House Rule"


class Room(core_models.TimeStampedModel):
    """Room Model Definition"""

    name = models.CharField(max_length=140)
    description = models.TextField()
    country = CountryField()
    city = models.CharField(max_length=100)
    price = models.IntegerField()
    address = models.CharField(max_length=140)
    beds = models.IntegerField()
    bath = models.IntegerField()
    guests = models.IntegerField()
    check_in = models.TimeField()
    check_out = models.TimeField()
    instant_book = models.BooleanField(default=False)
    # one top many (user to rooms)
    host = models.ForeignKey(user_models.User, on_delete=models.CASCADE)
    # host = models.ForeignKey("users.User", on_delete=models.CASCADE)
    roomtype = models.ForeignKey(RoomType, on_delete=models.SET_NULL, null=True)
    amenity = models.ManyToManyField(Amenity, blank=True)
    facility = models.ManyToManyField(Facility, blank=True)
    house_rules = models.ManyToManyField(HouseRule, blank=True)

    # name값을 Rooom 이름으로 표출
    def __str__(self):
        return self.name


class Photo(core_models.TimeStampedModel):
    """Photo Model Def."""

    caption = models.CharField(max_length=120)
    file = models.ImageField()
    room = models.ForeignKey(Room, on_delete=models.CASCADE)

    # name값을 Rooom 이름으로 표출
    def __str__(self):
        return self.caption
