# tweets/urls.py
from django.urls import path
from .views import PostListView, PostCreateView

urlpatterns = [
    path('posts/new/', PostCreateView.as_view(), name='post_new'),
    path('', PostListView.as_view(), name='home'),
]
