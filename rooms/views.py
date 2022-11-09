from math import ceil
from django.shortcuts import render
from django.core.paginator import Paginator
from . import models

def all_rooms(request):
    # Python만 사용해서  page 구현방식
    # page = request.GET.get("page", 1)
    # page = int(page or 1)
    # page_size = 10
    # limit = page_size * page
    # offset = limit - page_size
    # all_rooms = models.Room.objects.all()[offset:limit]
    # page_count = ceil(models.Room.objects.count() / page_size)
    
    page = request.GET.get("page",1)
    room_list = models.Room.objects.all()
    paginator = Paginator(room_list, 10, orphans=5)
    rooms = paginator.page(int(page))
    return render(request, "rooms/home.html", context={"page": rooms,},)
