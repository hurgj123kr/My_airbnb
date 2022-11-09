from django.shortcuts import render
from . import models as room_models

def all_rooms(request):
    page = int(request.GET.get("page", 1))
    page_size = 10
    limit = page_size * page
    offset = limit - page_size
    all_rooms = room_models.Room.objects.all()[offset:limit]
    return render(request, "rooms/home.html", context={"all_rooms": all_rooms})
