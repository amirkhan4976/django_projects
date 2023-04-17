from django.urls import path

from . import views

urlpatterns = [
    path("printnum/<slug:guess>", views.printnum, name="printnum"),
    path("", views.index, name="index"),
]

