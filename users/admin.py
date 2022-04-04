from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from . import models

# Register your models here.

# admin.site.register(models.User, CustomUserAdmin)


@admin.register(models.User)
class CustomUserAdmin(UserAdmin):

    """ Custom User Admin"""

    fieldsets = UserAdmin.fieldsets + (
        (
            'Custom Fields',
            {
                'fields': (
                    'avatar',
                    'gender',
                    'bio',
                    "birthdate",
                    "language",
                    "currency",
                    "superhost",
                )

            }
        ),
    )


# @admin.register(models.User)
# class CustomUserAdmin(admin.ModelAdmin):

#     """ Custom User Admin"""

#     list_display = (
#         'username', 'gender', 'language', 'currency', 'superhost'
#     )
#     list_filter = (
#         'language', 'currency', 'superhost'
#     )
