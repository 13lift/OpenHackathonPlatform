from django.urls import path

from lifter.hack.views import (
    hack_list_view,
    # hack_redirect_view,
    # hack_update_view,
    hack_detail_view,
)

app_name = "hack"
urlpatterns = [
    path("", view=hack_list_view, name="list"),
    # path("~update/", view=hack_update_view, name="update"),
    path("<str:slug>/", view=hack_detail_view, name="detail"),
]
