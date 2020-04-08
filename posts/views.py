from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView
from django.views.generic.edit import CreateView
from django.urls import reverse
from .models import Post

class PostListView(ListView):
    model = Post
    template_name = 'home.html'

class PostCreateView(CreateView):
    model = Post
    template_name = 'post_new.html'
    fields = ['user', 'body']

    def get_success_url(self):
        return reverse('home')
