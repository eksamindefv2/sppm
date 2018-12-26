from django.conf.urls import url
from Urusetia import views
from django.urls import path

urlpatterns = [
    #url(r'^$', views.HomePageView.as_view(), name='home'), # Notice the URL has been named
    # url(r'^about/$', views.AboutPageView.as_view(), name='about'),
    path('sesi/',views.SenaraiSesi,name='sesi_home'),
    path('sesi/new/',views.TambahSesi,name='sesi_new'),
    path('sesi/<int:pk>/edit/',views.EditSesi,name='sesi_edit'),

    path('sesi_list/',views.sesi_list,name='sesi_list'),
    path('sesi_list/create', views.sesi_create, name='sesi_create'),
    path('sesi/<int:pk>/update/', views.sesi_update, name='sesi_update'),

    #path('sistem/',views.sistem_list,name='sistem_list'),
]