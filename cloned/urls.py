from django.urls import path
from . import views

app_name = 'cloned'
urlpatterns = [
    path('', views.TweetListView.as_view(), name='home'),
    path('add/', views.TweetAddView.as_view(), name='add_tweet'),
    path('tweet/<int:pk>/like/', views.tweet_like, name='tweet_like'),
    path('tweet/<int:pk>/comment/', views.CommentAdd.as_view(), name='add_comment'),
]