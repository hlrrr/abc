from django.db import models
from core import models as core_models

# Create your models here.


class Reservation(core_models.TimeStampedModel):
    """Rervation Models Def."""

    STATUS_PAENDING = "pending"
    STATUS_CONFIRMED = "confirmed"
    STATUS_CANCELED = "canceled"

    STATUS_CHOICES = (
        (STATUS_PAENDING, "pending"),
        (STATUS_CONFIRMED, "confirmed"),
        (STATUS_CANCELED, "canceled"),
    )

    status = models.CharField(
        max_length=20, choices=STATUS_CHOICES, default=STATUS_PAENDING
    )
    guest = models.ForeignKey("users.User", on_delete=models.CASCADE)
    check_in = models.DateField()
    check_out = models.DateField()
    room = models.ForeignKey("rooms.Room", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.room} - {self.check_in}"
