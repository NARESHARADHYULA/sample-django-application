from . import views
from django.conf.urls import url

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^validate/$', views.validate, name='validate'),
    url(r'^viewdetails/$', views.viewdetails, name='viewdetails'),
]
