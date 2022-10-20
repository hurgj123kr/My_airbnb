from django.contrib import admin
from . import models

@admin.register(models.Reservation)
class ReservationAdmin(admin.ModelAdmin):

    """ Reservation Admin Definition """

    list_display = (
        "status",
        "check_in",
        "check_out",
        "guest",
        "room",
        "in_progress",
        "is_finished",
    )

    list_filter = ("status",)