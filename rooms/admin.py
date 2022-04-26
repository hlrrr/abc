from django.contrib import admin
from . import models
# Register your models here.


@admin.register(models.Room)
class RoomAdmin(admin.ModelAdmin):
    """Room admin Def."""

    fieldsets = (
        (
            "Basic info",
            {
                "classes": ("collapse",),
                "fields": ("name","host", "description", "country", "address", "price")},
        ),
        (
            "Times",
            {"fields": ("check_in","check_out"),}
        ),
        (
            "Spaces",
            {"fields": ("amenity","facility","house_rules")}
        ),
    )

    ordering = ("price",)

    list_display = (
        "name",
        "country",
        "city",
        "price",
        "address",
        "beds" ,
        "bath",
        "guests",
        "instant_book",
        "count_amenities",
        "count_photos",
    )

    list_filter = (
        "instant_book",
        "roomtype",
        "host__superhost",
    )

    search_fields = [
        "^city","^host__username"
    ]

    filter_horizontal = (
        "amenity",
        "facility",
        "house_rules",
    )

    def count_amenities(self, obj):
        return obj.amenity.count()
    #count_amenities.short_description = "new decription"

    def count_photos(self, obj):
        return  obj.photos.count()

@admin.register(models.RoomType, models.Facility, models.Amenity, models.HouseRule)
class ItemAdmin(admin.ModelAdmin):
    """Item Admin Def."""
    
    list_display = (
        "name", "used_by",
    )

    def used_by(self, obj):
        return obj.rooms.count()


@admin.register(models.Photo)
class PhotoAdmin(admin.ModelAdmin):
    """Photo Admin Def"""
    pass
