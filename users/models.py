from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    biography = models.CharField(max_length=250, blank=True, null=True)
    image = models.ImageField(upload_to="users/images", blank=True, null=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True)


