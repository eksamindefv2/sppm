from django.conf.urls import include,url
from . import views
from django.urls import path
from django.contrib.auth import views as auth_views

urlpatterns = [
    # path('sistem/',views.SenaraiSistem,name='sistem_home'),
    # path('sistem/new',views.Sistem_new,name='sistem_new'),
    path('daftar_pengguna',views.DaftarPengguna,name='daftar_pengguna'),
    # path('tambah_peranan', views.TambahPeranan, name='tambah_peranan'),
    path('landing_page',views.Landing_page,name='landing_page'),
    # url(r'^logout/$', auth_views.logout, name='logout'),
    # url(r'^about/$', views.AboutPageView.as_view(), name='about'),


    # CRUD django biasa
    # Source : https://github.com/wwiras/esertauat
    path('sistemdj/',views.sistemdj_list,name='sistemdj_list'),

    #Test bootstrap4 modal form from sibtc
    # Source : https://simpleisbetterthancomplex.com/tutorial/2016/11/15/how-to-implement-a-crud-using-ajax-and-json.html
    # Tambah page relaod sebab table adalah Datatables
    path('sistem/',views.sistem_list,name='sistem_list'),
    path('sistem/create', views.sistem_create, name='sistem_create'),
    path('sistem/<int:pk>/update/', views.sistem_update, name='sistem_update'),
    path('sistem/<int:pk>/delete/', views.sistem_delete, name='sistem_delete'),

]