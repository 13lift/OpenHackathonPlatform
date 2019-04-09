from django.conf.urls import url

from .views import *

urlpatterns = [
    url(r'^$', ProfilesList.as_view(), name='list'),
    url(r'^(?P<pk>\w+)/?$', ProfilesDetail.as_view(), name='detail'),
]
