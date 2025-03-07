from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from .models import Tweet, Follow
from django.db.models import Q

def feed(request):
    # Get the logged-in user
    user = request.user

    # Get the list of users that the logged-in user is following (including themselves)
    following_users = Follow.objects.filter(follower=user).values_list('followed', flat=True)
    following_users = list(following_users) + [user.id]  # Add the current user to the list of followed users

    # Get all tweets from followed users, ordered by creation date (newest first)
    tweets = Tweet.objects.filter(user_id__in=following_users).order_by('-created_at')

    # Render the feed with the tweets
    return render(request, 'tweets/feed.html', {'tweets': tweets})

def create_tweet(request):
    if request.method == 'POST':
        content = request.POST.get('content')
        tweet = Tweet(user=request.user, content=content)
        tweet.save()
        return redirect('feed')  # Redirect back to feed after creating a tweet
    return render(request, 'tweets/create_tweet.html')