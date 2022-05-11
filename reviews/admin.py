from django.contrib import admin
from . import models

# Register your models here.


@admin.register(models.Review)
class RevieAdmin(admin.ModelAdmin):
    """Review Admin Def."""

    list_display = ("__str__", "rating_average")
