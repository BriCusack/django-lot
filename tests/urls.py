# -*- coding: utf-8 -*-

from django.urls import path, re_path, include

from .tests import TestView


urlpatterns = path("",
    re_path(r"", include('lot.urls')),
    re_path(r"^test_url/$", TestView.as_view()),
)
