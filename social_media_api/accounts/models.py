from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    bio = models.TextField(blank=True, null=True)
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True, null=True)
    followers = models.ManyToManyField('self', symmetrical=False, related_name='following')

    def __str__(self):
        return self.username
    
    def follow(self, user):
        """Follow another user."""
        if user != self:
            self.followers.add(user)

    def unfollow(self, user):
        """Unfollow another user."""
        if user != self:
            self.followers.remove(user)

    def is_following(self, user):
        """Check if the user is following a specific user."""
        return self.following.filter(id=user.id).exists()