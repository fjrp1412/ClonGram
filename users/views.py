# Django imports
from django.shortcuts import render
from django.contrib.auth import views as auth_views
from django.views.generic import DetailView
from django.views.generic.edit import FormView, UpdateView
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy, reverse

# Local imports
from posts.models import Posts
from users.forms import SignUpForm
from users.models import Profile


class LoginView(auth_views.LoginView):
    template_name = "users/login.html"

    redirect_authenticated_user = True


class LogoutView (auth_views.LogoutView):
    pass


class UserDetailView(LoginRequiredMixin, DetailView):
    template_name = "users/user.html"
    slug_field = "username"
    slug_url_kwarg = "username"
    model = User
    queryset = User.objects.all()
    context_object_name = "user"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.get_object()
        context["posts"] = Posts.objects.filter(
            user_id=user).order_by("-created")
        return context


class SignUpView(FormView):
    template_name = "users/sign-up.html"
    form_class = SignUpForm
    success_url = reverse_lazy("users:login")

    def form_valid(self, form):
        print(form)
        form.save()
        return super().form_valid(form)


class UpdateProfileView(LoginRequiredMixin, UpdateView):
    model = Profile
    template_name = "users/update.html"
    fields = ["image"]

    def get_object(self, queryset=None):
        return self.request.user.profile

    def get_success_url(self):
        username = self.object.user.username
        return reverse("users:detail", kwargs={"username": username})
