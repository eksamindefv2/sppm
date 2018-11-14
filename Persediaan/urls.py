from django.conf.urls import include,url
from . import views
from django.urls import path

urlpatterns = [
    path('sistem/',views.SenaraiSistem,name='sistem_home'),
    # url(r'^about/$', views.AboutPageView.as_view(), name='about'),
]