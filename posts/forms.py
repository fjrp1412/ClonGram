from django import forms
from posts.models import Posts
from django.contrib.auth.models import User
from users.models import Profile


class CreatePostModelForm(forms.ModelForm):
    class Meta:
        model = Posts
        fields = ("user_id", "image", "title", "profile_id")
