from django.shortcuts import render
from django.contrib.auth import views as auth_views
from django.views.generic import DetailView
from django.contrib.auth.models import User
from posts.models import Posts
# Create your views here.


class LoginView(auth_views.LoginView):
    template_name = "users/login.html"

    redirect_authenticated_user = True

class UserDetailView(DetailView):
    template_name = "users/user.html"
    slug_field = "username"
    slug_url_kwarg = "username"
    model = User
    queryset = User.objects.all()
    context_object_name = "user"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.get_object()
        context["posts"] = Posts.objects.filter(user_id=user).order_by("-created")
        return context
    
