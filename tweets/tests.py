from django.test import TestCase
from django.contrib.auth.models import User
from .models import Tweet, Profile, Follow, Like, Retweet


class SocialMediaTestCase(TestCase):
    def setUp(self):
        # Clean up any existing profiles and users before the tests run
        Profile.objects.all().delete()
        User.objects.all().delete()

        # Create mock users
        self.user1 = User.objects.create_user(username='user1', password='password1')
        self.user2 = User.objects.create_user(username='user2', password='password2')

        # Use get_or_create to avoid duplicates
        self.profile1, created = Profile.objects.get_or_create(user=self.user1)
        self.profile2, created = Profile.objects.get_or_create(user=self.user2)

        # Create mock tweets
        self.tweet1 = Tweet.objects.create(user=self.user1, content="This is a tweet by user1.")
        self.tweet2 = Tweet.objects.create(user=self.user2, content="This is a tweet by user2.")

    def test_create_profile(self):
        """Test if user profile is created successfully after registration."""
        self.assertEqual(self.profile1.user.username, 'user1')
        self.assertEqual(self.profile2.user.username, 'user2')
        self.assertTrue(Profile.objects.filter(user=self.user1).exists())
        self.assertTrue(Profile.objects.filter(user=self.user2).exists())

    def test_follow_user(self):
        """Test if user can follow another user."""
        # User1 follows User2
        Follow.objects.create(follower=self.user1, following=self.user2)
        self.assertTrue(Follow.objects.filter(follower=self.user1, following=self.user2).exists())

    def test_unfollow_user(self):
        """Test if user can unfollow another user."""
        follow = Follow.objects.create(follower=self.user1, following=self.user2)
        follow.delete()
        self.assertFalse(Follow.objects.filter(follower=self.user1, following=self.user2).exists())

    def test_like_tweet(self):
        """Test if user can like a tweet."""
        # User1 likes User2's tweet
        Like.objects.create(user=self.user1, tweet=self.tweet2)
        self.assertTrue(Like.objects.filter(user=self.user1, tweet=self.tweet2).exists())

    def test_unlike_tweet(self):
        """Test if user can unlike a tweet."""
        like = Like.objects.create(user=self.user1, tweet=self.tweet2)
        like.delete()
        self.assertFalse(Like.objects.filter(user=self.user1, tweet=self.tweet2).exists())

    def test_retweet(self):
        """Test if user can retweet a tweet."""
        # User1 retweets User2's tweet
        Retweet.objects.create(user=self.user1, tweet=self.tweet2)
        self.assertTrue(Retweet.objects.filter(user=self.user1, tweet=self.tweet2).exists())

    def test_unretweet(self):
        """Test if user can unretweet a tweet."""
        retweet = Retweet.objects.create(user=self.user1, tweet=self.tweet2)
        retweet.delete()
        self.assertFalse(Retweet.objects.filter(user=self.user1, tweet=self.tweet2).exists())

    def test_feed_display(self):
        """Test if feed displays the tweets of the users the logged-in user follows."""
        # User1 follows User2
        Follow.objects.create(follower=self.user1, following=self.user2)
        
        # Check if tweet from followed user appears in the feed
        response = self.client.login(username='user1', password='password1')
        response = self.client.get('/api/feed/')
        self.assertContains(response, self.tweet2.content)
