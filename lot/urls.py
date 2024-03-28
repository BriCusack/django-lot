# -*- coding: utf-8 -*-

from django.urls import path, re_path

from . import views

urlpatterns = [
    path("login/<uuid:uuid>/", views.LOTLogin.as_view(), name="login"),
]

