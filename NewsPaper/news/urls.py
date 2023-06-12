from django.urls import path
from .views import Post, PostDetailView, PostListView


urlpatterns = [

    path('', PostListView.as_view()),
    path('<int:pk>/', PostDetailView.as_view()),
    path('post/<int:post_id>/', PostDetailView.as_view(), name='post_detail'),
]