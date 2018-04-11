from django.urls import path 
from django.contrib.auth import views as auth_views

from . import views

app_name = 'accounts'
urlpatterns = [
   path('user/signup/', views.SignUpView.as_view(), name='signup'),
   path('u/<slug:username>/detail/', views.DetailAccountView.as_view(), name='account_detail'),
   path('u/<slug:username>/update/', views.UpdateAccountView.as_view(), name='account_update'),
   path('u/<slug:username>/following/', views.FollowingListView.as_view(), name='following'),
   path('u/<slug:username>/followers/', views.FollowersListView.as_view(), name='followers'),
   
 ]