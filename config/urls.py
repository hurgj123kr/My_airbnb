import uuid
import os
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static

def trigger_error(request):
    division_by_zero = 1 / 0

urlpatterns = [
    path("",include("core.urls", namespace="core")),
    path("lists/",include("lists.urls", namespace="lists")),
    path("rooms/",include("rooms.urls", namespace="rooms")),
    path("users/",include("users.urls", namespace="users")),
    path("reviews/",include("reviews.urls", namespace="reviews")),
    path("reservations/",include("reservations.urls", namespace="reservations")),
    path("conversations/",include("conversations.urls", namespace="conversations")),
    path(os.environ.get(f"DJANGO_ADMIN+{uuid.uuid4().hex[:10]}", "admin/"), admin.site.urls),
    path("sentry-debug/", trigger_error),
]

#개발 환경이 맞을경우 이미지 저장경로는 MEDIA_URL이며, 폴더는 MEDOA_ROOT로 함.
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)