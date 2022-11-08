from datetime import datetime
from django.shortcuts import render

def all_rooms(request):
    
    now = datetime.now()

    return render(request, "all_rooms.html",{"now": now})
