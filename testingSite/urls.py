from django.conf.urls import url, include
from django.contrib import admin

from . import views
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    #url(r'^oauth2callback', views.auth_return, "auth2callback"),
    url(r'verify$', views.verify),
    #url(r'^$', views.index),
    #url(r'^api/', include('testingSite.api.urls', namespace='api')),
]