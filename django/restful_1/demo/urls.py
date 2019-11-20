from django.conf.urls import url
from demo import views

urlpatterns = [
    url(r'^user/$', views.User_list),
    url(r'^user/(?P<pk>[0-9]+)/$', views.User_detial),
]