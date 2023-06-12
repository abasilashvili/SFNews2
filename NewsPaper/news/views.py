from django.views.generic import ListView, DetailView
from .models import Post, PostCategory
from datetime import datetime
from django.shortcuts import get_object_or_404, render


class PostListView(ListView):

    model = Post

    ordering = '-creation_date_time'

    template_name = 'posts.html'

    context_object_name = 'posts'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['time_now'] = datetime.utcnow()
        context['next_sale'] = "Репортаж в среду!"
        context['news'] = Post.objects.all()
        return context


class PostDetailView(DetailView):
    model = Post
    template_name = 'post.html'
    context_object_name = 'post'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['time_now'] = datetime.utcnow()
        context['next_sale'] = "Репортаж в среду!"
        context['news'] = Post.objects.all()
        return context

    def post_detail(request, post_id):
        post = get_object_or_404(Post, pk=post_id)
        return render(request, 'news/post.html', {'post': post})


