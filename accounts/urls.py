from django.urls import path 
from django.contrib.auth import views as auth_views

from . import views

app_name = 'accounts'
urlpatterns = [
   #path('user/login/', views.login, {'template_name': 'accounts/login.html'}, name='login'),
   #path('user/logout/', auth_views.logout, {'next_page': 'cloned:home'}, name='logout'),
   path('user/signup/', views.SignUp.as_view(), name='signup'),

 ]