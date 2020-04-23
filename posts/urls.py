# tweets/urls.py
from django.urls import path
from .views import PostListView, PostCreateView, TextListView, TextCreateView
# from .views import TextListView, TextCreateView

urlpatterns = [
    path('posts/new/', PostCreateView.as_view(), name='post_new'),
    path('', PostListView.as_view(), name='home'),
    path('posts/new/', TextCreateView.as_view(), name='text_new'),
    path('', TextListView.as_view(), name='home'),
]
# urlpatterns = [
#     path('posts/new/', TextCreateView.as_view(), name='post_new'),
#     path('', TextListView.as_view(), name='home'),
# ]
