from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from django.urls import path

from tweets import views

urlpatterns = [
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('feed/', views.feed, name='feed'),
    path('create/', views.create_tweet, name='create_tweet'),
]