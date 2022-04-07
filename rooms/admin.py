from django.contrib import admin
from . import models
# Register your models here.


@admin.register(models.Room)
class RoomAdmin(admin.ModelAdmin):
    """Room admin Def."""

    pass


@admin.register(models.RoomType, models.Facility, models.Amenity, models.HouseRule)
class ItemAdmin(admin.ModelAdmin):
    """Item Admin Def."""
    pass


@admin.register(models.Photo)
class PhotoAdmin(admin.ModelAdmin):
    """Photo Admin Def"""
    pass
