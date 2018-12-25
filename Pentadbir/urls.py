from django.conf.urls import include,url
from . import views
from django.urls import path
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('sistem/',views.SenaraiSistem,name='sistem_home'),
    path('sistem/new',views.Sistem_new,name='sistem_new'),
    path('daftar_pengguna',views.DaftarPengguna,name='daftar_pengguna'),
    # path('tambah_peranan', views.TambahPeranan, name='tambah_peranan'),
    path('landing_page',views.Landing_page,name='landing_page'),
    # url(r'^logout/$', auth_views.logout, name='logout'),
    # url(r'^about/$', views.AboutPageView.as_view(), name='about'),

    #Test bootstrap form
    path('sistemlist/',views.senaraisis,name='sistemlist'),
    # path('create/', views.SisCreateView.as_view(), name='create_sis'),
    path('sistem/create', views.sistem_create, name='sistem_create'),
    path('sistem/<int:pk>/update/', views.sistem_update, name='sistem_update'),
    path('sistem/<int:pk>/delete/', views.sistem_delete, name='sistem_delete'),

]