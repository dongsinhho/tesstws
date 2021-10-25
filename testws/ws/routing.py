from django.urls import path

from .consumer import WSConsummer

websocket_urlpatterns = [
    path("", WSConsummer.as_asgi()),
]
