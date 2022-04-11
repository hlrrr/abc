from random import choices
from django.db import models
from core import models as core_models

# Create your models here.


class Reservation(core_models.TimeStampedModel):

    STATUS_PENDING = "pending"
    STATUS_CONFIRMED = "confirmed"
    STATUS_CANCELD = "canceled"

    STATUS_CHOICE = (
        (STATUS_PENDING, "pending"),
        (STATUS_CONFIRMED, "confirmed"),
        (STATUS_CANCELD, "canceled"),
    )

    status = models.CharField(
        max_length=22, choices=STATUS_CHOICE, default=STATUS_PENDING)
    guest = models.ForeignKey("users.User", on_delete=models.CASCADE)
    room = models.ForeignKey("rooms.Room", on_delete=models.CASCADE)
    check_in = models.DateField()
    check_out = models.DateField()

    def __str__(self):
        return f"{self.room}-{self.check_in}"
