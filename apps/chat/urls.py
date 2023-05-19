from django.urls import path
from .views import RoomView, IndexView

urlpatterns = [
    path("", IndexView.as_view(), name="index"),
    path("<str:room_name>/", RoomView.as_view(), name="room"),
]
