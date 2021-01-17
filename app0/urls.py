from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [

     path('',views.index1),
     path('users', views.users),
     path('ind', views.ind),
     path('list', views.list),

     path(r'^search/$', views.search, name='search'),
     url(r'^(?P<user_id>[0-9]+)/$', views.detail_element, name='detail_name'),
     path(r'^ajouter/$', views.ajouter, name='ajouter'),
       # path('<int:user_id>/', views.detail_element, name='detail_name')





]