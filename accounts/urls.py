from django.urls import path 
from django.contrib.auth import views as auth_views

from . import views

app_name = 'accounts'
urlpatterns = [
   path('user/signup/', views.SignUp.as_view(), name='signup'),

 ]