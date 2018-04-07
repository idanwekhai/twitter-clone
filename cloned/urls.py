from django.urls import path
from . import views

app_name = 'cloned'
urlpatterns = [
    path('', views.TweetListView.as_view(), name='home'),
    path('add/', views.TweetAddView.as_view(), name='add_tweet'),
    path('tweet/<int:pk>/like/', views.TweetLikeView, name='tweet_like'),
    path('tweet/<int:pk>/comment/', views.CommentAddView.as_view(), name='add_comment'),
    path('tweet/<int:pk>/edit', views.TweetEditView.as_view(), name='edit_tweet')
]