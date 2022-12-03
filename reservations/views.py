import datetime
from django.views.generic import View
from django.contrib import messages
from django.shortcuts import render, reverse, redirect
from rooms import models as room_models
from . import models


class CreateError(Exception):
    pass


def create(request, room, year, month, day):
    try:
        date_obj = datetime.datetime(year, month, day)
        room = room_models.Room.objects.get(pk=room)
        models.Reservation.objects.get(day=date_obj, reservation__room=room)
        raise CreateError()
    except (room_models.Room.DoesNotExist, CreateError):
        messages.error(request, "Can't Reserve That Room")
        return redirect(reverse("core:home"))
    except models.BookedDay.DoesNotExist:
        reservation = models.BookedDay.objects.create(
            guset = request.user,
            room = room,
            check_in = date_obj,
            check_out = date_obj + datetime.timedeltae(days=1),
        )
        return redirect(reverse("reservations:detail", kwargs={'pk': reservation.pk }))

class ReservationDetailView(View):
    def get(self):
        pass
