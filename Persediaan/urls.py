from django.conf.urls import include,url
from . import views
from django.urls import path

urlpatterns = [
    path('sistem/',views.SenaraiSistem,name='sistem_home'),
    path('sistem/new',views.Sistem_new,name='sistem_new'),
    # url(r'^about/$', views.AboutPageView.as_view(), name='about'),
]