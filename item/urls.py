from django.conf.urls import url

from . import views

app_name = "Item"

urlpatterns = [
    url(r'^(?P<region_selected>[-\w]+)/$', views.get_travel_data, name = 'travel_data'),
]
