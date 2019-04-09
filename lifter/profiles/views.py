from .models import *
import pdb

from django.core.urlresolvers import reverse
from django.views.generic import DetailView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import *
from django.utils import timezone


class ProfilesList(ListView):
    model = Profile
    paginate_by = 30


class ProfilesDetail(DetailView):
    model = Profile
