from typing import Any, Dict
from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
# chat/views.py



class IndexView(TemplateView):
    template_name = "chat/index.html"


class RoomView(TemplateView):
    template_name = "chat/room.html"

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        ctx = super().get_context_data(**kwargs)
        ctx["room_name"] = self.kwargs["room_name"]
        return ctx


def index(request):
    return render(request, "chat/index.html")
