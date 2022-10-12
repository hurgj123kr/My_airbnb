from django.contrib import admin
from . import models


@admin.register(models.RoomType)
class ItemAdmin(admin.ModelAdmin):
    """ Item Admin Definition """
    pass

@admin.register(models.Room)
class RoomAdmin(admin.ModelAdmin):

    """ Room Admin Definition """

    pass
