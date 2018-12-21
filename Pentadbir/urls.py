from django.conf.urls import include,url
from . import views
from django.urls import path
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('sistem/',views.SenaraiSistem,name='sistem_home'),
    path('sistem/new',views.Sistem_new,name='sistem_new'),
    path('daftar_pengguna',views.DaftarPengguna,name='daftar_pengguna'),
    path('hapus_pengguna/<int:pk>',views.HapusPengguna,name='hapus_pengguna'),
    # path('tambah_peranan', views.TambahPeranan, name='tambah_peranan'),
    path('landing_page',views.Landing_page,name='landing_page'),
    # url(r'^logout/$', auth_views.logout, name='logout'),
    # url(r'^about/$', views.AboutPageView.as_view(), name='about'),
]