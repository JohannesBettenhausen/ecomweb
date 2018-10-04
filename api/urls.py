from django.conf.urls import url
from api import views

urlpatterns = [
    url(r'^messdaten/$', views.snippet_list),
    url(r'^messdaten/(?P<pk>[0-9]+)/$', views.snippet_detail),
]