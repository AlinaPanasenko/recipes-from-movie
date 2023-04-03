from django.shortcuts import render, get_object_or_404
from .models import Post
from .forms import CommentForm
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)


def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'main.html', context)


class PostList(ListView):
    model = Post
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'main.html'
    context_object_name = 'posts'
    paginate_by = 6


class PostDetail(DetailView):
    model = Post
    template_name = "post_detail.html"


class PostCreate(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'recipe']
    template_name = 'post_form.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdate(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'recipe']
    template_name = 'post_form.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class PostDelete(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    template_name = 'post_confirm_delete.html'
    success_url = ''

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False
