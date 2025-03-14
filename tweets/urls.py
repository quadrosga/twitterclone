from django.urls import path, include
from django.views.generic.base import RedirectView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from django.contrib.auth.views import LoginView, LogoutView
from tweets import views

urlpatterns = [
    # Redirect root URL to the login page
    path('', RedirectView.as_view(url='/login/', permanent=True)),

    # JWT endpoints
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    # Tweet-related endpoints
    path('feed/', views.feed, name='feed'),
    path('post/', views.create_tweet, name='post_tweet'),
    path('follow/<int:user_id>/', views.follow, name='follow'),
    path('unfollow/<int:user_id>/', views.unfollow, name='unfollow'),
    path('like/<int:tweet_id>/', views.like_tweet, name='like_tweet'),
    path('unlike/<int:tweet_id>/', views.unlike_tweet, name='unlike_tweet'),
    path('reply/<int:tweet_id>/', views.reply_to_tweet, name='reply_to_tweet'),
    path('retweet/<int:tweet_id>/', views.retweet, name='retweet'),
    path('unretweet/<int:tweet_id>/', views.unretweet, name='unretweet'),

    # Authentication endpoints
    path('accounts/', include('django.contrib.auth.urls')),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', views.register, name='register'),
]