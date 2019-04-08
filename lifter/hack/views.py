from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
from django.views.generic import DetailView, ListView, RedirectView, UpdateView
from lifter.hack.models import Hackathon

User = get_user_model()


class HackDetailView(LoginRequiredMixin, DetailView):

    model = Hackathon
    slug_field = "slug"
    slug_url_kwarg = "slug"

hack_detail_view = HackDetailView.as_view()


class HackListView(LoginRequiredMixin, ListView):

    model = Hackathon
    slug_field = "slug"
    slug_url_kwarg = "slug"

hack_list_view = HackListView.as_view()
