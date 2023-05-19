from django.shortcuts import render, redirect
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from rules.contrib.views import PermissionRequiredMixin

from .models import Post
from .forms import PostForm


# Create your views here.
class PostListView(ListView):
    template_name = "post/list.html"
    model = Post
    paginate_by = 10


class PostDetailView(DetailView):
    template_name = "post/detail.html"
    model = Post


class PostCreateView(CreateView):
    model = Post
    template_name = "post/form.html"
    success_url = reverse_lazy("post:list")
    fields = ["body"]

    def form_valid(self, form: PostForm):
        post: Post = form.save(commit=False)
        post.user = self.request.user
        post.save()
        return super().form_valid(form)


class PostUpdateView(PermissionRequiredMixin, UpdateView):
    model = Post
    template_name = "post/form.html"
    success_url = reverse_lazy("post:list")
    permission_required = "post.can_update"
    fields = ["body"]

    def form_valid(self, form: PostForm):
        post: Post = form.save(commit=False)
        post.user = self.request.user
        post.save()
        return super().form_valid(form)


class PostDeleteView(DeleteView, PermissionRequiredMixin):
    model = Post
    template_name = "post/delete.html"
    permission_required = "post:can_update"
    success_url = reverse_lazy("post:list")
