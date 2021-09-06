from django.shortcuts import render
from django.views import generic
from posts.models import Posts
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.


class PostsFeedView(LoginRequiredMixin, generic.ListView):
    template_name = "posts/index.html"
    model = Posts
    context_object_name = "posts"
