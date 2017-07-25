from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^allreadings/$', views.AllReadingsListView.as_view(), name='all_readings_list'),
    url(r'^readings/$', views.CurrentReading, name='readings_list'),
]
