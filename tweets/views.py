from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import Like, Profile, Retweet, Tweet, Follow
from django.db.models import Q


def feed(request):
    user = request.user

    # Get the user's profile
    profile = Profile.objects.get(user=user)

    # Get the list of users that the logged-in user is following (including themselves)
    following_users = Follow.objects.filter(follower=user).values_list('following', flat=True)
    following_users = list(following_users) + [user.id]  # Add the current user to the list of followed users

    # Get all tweets from followed users, ordered by creation date (newest first)
    tweets = Tweet.objects.filter(user_id__in=following_users).order_by('-created_at')

    # Add an `is_liked` and `is_retweeted` attribute to each tweet
    liked_tweet_ids = Like.objects.filter(user=user).values_list('tweet_id', flat=True)
    retweeted_tweet_ids = Retweet.objects.filter(user=user).values_list('tweet_id', flat=True)

    # Get some users to suggest (excluding the logged-in user and already followed users)
    suggested_users = User.objects.exclude(id__in=list(following_users) + [user.id]).order_by('?')[:5]

    for tweet in tweets:
        tweet.is_liked = tweet.id in liked_tweet_ids
        tweet.is_retweeted = tweet.id in retweeted_tweet_ids
        tweet.is_followed = Follow.objects.filter(follower=user, following=tweet.user).exists()

    return render(request, 'tweets/feed.html', {
        'tweets': tweets,
        'suggested_users': suggested_users  # Send to template
    })


@login_required
def create_tweet(request):
    if request.method == 'POST':
        content = request.POST.get('content')
        if content:
            Tweet.objects.create(user=request.user, content=content)
        return redirect('feed')
    return render(request, 'tweets/create_tweet.html')

@login_required
def follow(request, user_id):
    user_to_follow = User.objects.get(id=user_id)
    
    if request.user != user_to_follow:
        Follow.objects.get_or_create(follower=request.user, following=user_to_follow)
        
    return redirect('feed')

@login_required
def unfollow(request, user_id):
    user_to_unfollow = User.objects.get(id=user_id)
    
    if request.user != user_to_unfollow:
        Follow.objects.filter(follower=request.user, following=user_to_unfollow).delete()
    
    return redirect('feed')

@login_required
def like_tweet(request, tweet_id):
    tweet = Tweet.objects.get(id=tweet_id)
    Like.objects.get_or_create(user=request.user, tweet=tweet)
    return redirect('feed')

@login_required
def unlike_tweet(request, tweet_id):
    tweet = Tweet.objects.get(id=tweet_id)
    Like.objects.filter(user=request.user, tweet=tweet).delete()
    return redirect('feed')

@login_required
def reply_to_tweet(request, tweet_id):
    parent_tweet = Tweet.objects.get(id=tweet_id)
    if request.method == 'POST':
        content = request.POST.get('content')
        tweet = Tweet(user=request.user, content=content, parent_tweet=parent_tweet)
        tweet.save()
        return redirect('feed')
    return render(request, 'tweets/reply_to_tweet.html', {'parent_tweet': parent_tweet})

@login_required
def retweet(request, tweet_id):
    tweet = Tweet.objects.get(id=tweet_id)
    Retweet.objects.get_or_create(user=request.user, tweet=tweet)
    return redirect('feed')

@login_required
def unretweet(request, tweet_id):
    tweet = Tweet.objects.get(id=tweet_id)
    Retweet.objects.filter(user=request.user, tweet=tweet).delete()
    return redirect('feed')