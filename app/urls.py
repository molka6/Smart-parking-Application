from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [

  path('',views.index),
  path('base',views.base),  
  path('index',views.index), 
]