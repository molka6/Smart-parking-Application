from django.urls import path
from django.conf.urls import url
from . import views
from login_user.views import user_logout


urlpatterns = [
     path('',views.index1, name='index1'),
     path('users', views.users),
     # path('ind', views.ind),
     path('list', views.list, name='list'),
     url(r'^(?P<user_id>[0-9]+)/$', views.detail_element, name='detail_name'),
     path('delete/<int:user_id>/', views.delete, name='delete'),
     path('edit/<int:user_id>/', views.edit, name='edit'),
     url(r'^ajouter/$', views.ajouter, name='ajouter'),
     path('search/', views.search, name='search'),
     path('work/', views.work, name='work'),

   
     
]