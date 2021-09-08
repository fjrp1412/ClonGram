from django.shortcuts import render
from django.views import generic
from posts.models import Posts
from django.views.generic.edit import FormView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from posts.forms import CreatePostModelForm

# Create your views here.


class PostsFeedView(LoginRequiredMixin, generic.ListView):
    template_name = "posts/index.html"
    model = Posts
    context_object_name = "posts"
    ordering = ["-created"]


class CreatePostView(LoginRequiredMixin, FormView):
    template_name = "posts/post.html"
    success_url = reverse_lazy('posts:feed')
    form_class = CreatePostModelForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["user"] = self.request.user
        context["profile"] = self.request.user.profile
        return context

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
