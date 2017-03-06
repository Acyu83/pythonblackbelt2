from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.index),
    url(r'^regis_process$', views.process),
    url(r'^login_process$', views.login),
    url(r'^success$', views.success),
    url(r'^logout$', views.logout),
    url(r'^add_process/(?P<id>\d+)$', views.add_process),
    url(r'^view/(?P<id>\d+)$', views.view_friend),
    url(r'^delete_process/(?P<id>\d+)$', views.delete_process),
    url(r'^', views.error)
]
