# -*- coding: utf-8 -*-

from django.urls import path, re_path

from . import views

urlpatterns = path("",
    re_path(r"^login/(?P<uuid>[\da-f]{8}-([\da-f]{4}-){3}[\da-f]{12})/$", views.LOTLogin.as_view(), name="login"),
)
