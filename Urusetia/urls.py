from django.conf.urls import url
from Urusetia import views
from django.urls import path

urlpatterns = [
    #url(r'^$', views.HomePageView.as_view(), name='home'), # Notice the URL has been named
    # url(r'^about/$', views.AboutPageView.as_view(), name='about'),
    path('sesi/',views.SenaraiSesi,name='sesi_home'),
    path('sesi/new/',views.TambahSesi,name='sesi_new'),
    path('sesi/<int:pk>/edit/',views.EditSesi,name='sesi_edit'),
]