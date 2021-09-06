from django.db import models
from django.contrib.auth.models import User
from users.models import Profile
from django.utils import timezone

class Posts(models.Model):
    image = models.ImageField(
        upload_to="posts/images", blank=False, null=False)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    profile_id = models.ForeignKey(Profile, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    created = models.DateTimeField(default=timezone.now)
