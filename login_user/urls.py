from django.urls import path
from . import views
from login_user.views import home
urlpatterns = [
    
    path('login',views.user_login, name='login'),       
    path('index',views.index, name='index'),
    path("", home, name="homepage"),
    path("",views.user_logout, name='logout'),
    
]
