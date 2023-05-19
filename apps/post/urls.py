from django.urls import path
from .views import (
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
)

app_name = "post"
urlpatterns = [
    path("", PostListView.as_view(), name="list"),
    path("create/", PostCreateView.as_view(), name="create"),
    path("<str:pk>/", PostDetailView.as_view(), name="detail"),
    path("<str:pk>/update/", PostUpdateView.as_view(), name="update"),
    path("<str:pk>/delete/", PostDeleteView.as_view(), name="delete"),
]
