from django.conf.urls import include,url
from . import views
from django.urls import path
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('sistem/',views.SenaraiSistem,name='sistem_home'),
    path('peranan/',views.SenaraiPeranan,name='peranan_home'),
    path('statusnilai/',views.SenaraiStatusNilai,name='statusnilai_home'),
    path('sistem/new',views.Sistem_new,name='sistem_new'),
    path('refperanan/new',views.Peranan_new,name='peranan_new'),#reen tambah
    path('refperanan/edit/<int:pk>',views.Peranan_edit,name='peranan_edit'),#wira tambah
    path('refperanan/delete/<int:pk>',views.Peranan_delete,name='peranan_delete'),#wira tambah
    path('refstatusnilai/new',views.StatusNilai_new,name='statusnilai_new'),#reen tambah
    path('refstatusnilai/edit/<int:pk>',views.StatusNilai_edit,name='statusnilai_edit'),#reen tambah
    path('refstatusnilai/delete/<int:pk>',views.StatusNilai_delete,name='statusnilai_delete'),#reen tambah
    path('daftar_pengguna',views.DaftarPengguna,name='daftar_pengguna'),
    path('landing_page',views.Landing_page,name='landing_page'),
    # url(r'^logout/$', auth_views.logout, name='logout'),
    # url(r'^about/$', views.AboutPageView.as_view(), name='about'),
]