from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<entry>", views.entry, name="entry"),
    path("new", views.new, name="new"),
    path("random", views.random, name="random")
]
