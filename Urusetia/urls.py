from django.conf.urls import include,url
from Urusetia import views
from . import views
from django.urls import path
from django.contrib.auth import views as auth_views

urlpatterns = [
    url(r'^$', views.HomePageView.as_view(), name='home'), # Notice the URL has been named
    # url(r'^about/$', views.AboutPageView.as_view(), name='about'),
    path('auditee/',views.SenaraiAuditee,name='auditee_home'),
    path('auditee/new',views.auditee_new,name='auditee_new'),
    path('auditee/<int:pk>/edit/', views.auditee_edit, name='auditee_edit'),
    path('auditee/<int:pk>/remove/', views.auditee_remove, name='auditee_remove'),
]