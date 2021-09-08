from django.urls import path, include
from posts import views
urlpatterns = [
    path(
        route="",
        view=views.PostsFeedView.as_view(),
    ),
    path(
        route="posts/",
        view=views.PostsFeedView.as_view(),
        name="feed"
    ),
    path(
        route="new/",
        view=views.CreatePostView.as_view(),
        name="create"
    )

]
