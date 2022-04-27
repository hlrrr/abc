from django.contrib import admin
from . import models
# Register your models here.


@admin.register(models.Reservation)
class ReservationAdim(admin.ModelAdmin):

    """Reservation Model Def."""
    pass
