#-*- coding: utf-8 -*-
from django.conf.urls import url

import views

urlpatterns = [
  url(r'^$', views.index, name='index'),
  url(r'^profile/$', views.profile, name='profile'),
]