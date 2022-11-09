from django.views.generic import ListView
from django.urls import reverse
from django.shortcuts import render,redirect
from . import models


class HomeView(ListView):

    """ Home view Definition """

    model = models.Room
    paginate_by = 10
    paginate_orphans = 5
    ordering = "created"
    context_object_name = "rooms"

def room_detail(request, pk):
    
    try:
        room = models.Room.objects.get(pk=pk)
        return render(request, "rooms/detail.html", context={"room":room})
    except models.Room.DoesNotExist:
        return redirect(reverse("core:home"))   
    return render(request, "rooms/detail.html")





    # django +python 구현 방식
# def all_rooms(request):
#     page = request.GET.get("page",1)
#     room_list = models.Room.objects.all()
#     paginator = Paginator(room_list, 10, orphans=5)
#     try:
#         rooms = paginator.page(int(page))
#         return render(request, "rooms/home.html", context={"page": rooms,},)
#     except EmptyPage:
#         return redirect("/")

    # Python만 사용해서  page 구현방식
    # page = request.GET.get("page", 1)
    # page = int(page or 1)
    # page_size = 10
    # limit = page_size * page
    # offset = limit - page_size
    # all_rooms = models.Room.objects.all()[offset:limit]
    # page_count = ceil(models.Room.objects.count() / page_size)

