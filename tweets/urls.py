from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from django.urls import include, path

from tweets import views

urlpatterns = [
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('feed/', views.feed, name='feed'),
    path('post/', views.create_tweet, name='post_tweet'),
    path('follow/<int:user_id>/', views.follow, name='follow'),
    path('unfollow/<int:user_id>/', views.unfollow, name='unfollow'),
    path('like/<int:tweet_id>/', views.like_tweet, name='like_tweet'),
    path('unlike/<int:tweet_id>/', views.unlike_tweet, name='unlike_tweet'),
    path('reply/<int:tweet_id>/', views.reply_to_tweet, name='reply_to_tweet'),
    path('retweet/<int:tweet_id>/', views.retweet, name='retweet'),
    path('unretweet/<int:tweet_id>/', views.unretweet, name='unretweet'),
    path('accounts/', include('django.contrib.auth.urls')),
]