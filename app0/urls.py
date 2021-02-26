from django.urls import path
from django.conf.urls import url
from . import views
from login_user.views import user_logout


urlpatterns = [
 # path('<int:user_id>/', views.detail_element, name='detail_name')
     path('',views.index1),
     path('users', views.users),
     path('ind', views.ind),
     path('list', views.list),


     url(r'^search/$', views.search, name='search'),
     url(r'^(?P<user_id>[0-9]+)/$', views.detail_element, name='detail_name'),

     path('delete/<int:user_id>/', views.delete, name='delete'),

     url(r'^ajouter/$', views.ajouter, name='ajouter'),
       # path('<int:user_id>/', views.detail_element, name='detail_name')



]