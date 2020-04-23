from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView
from django.views.generic.edit import CreateView
from django.urls import reverse
from .models import Post, Textbook
# from .models import Textbook


class PostListView(ListView):
    model = Post
    template_name = 'home.html'

class PostCreateView(CreateView):
    model = Post
    template_name = 'post_new.html'
    fields = ['user', 'body', 'title', 'author', 'new']

    def get_success_url(self):
        return reverse('home')

class TextListView(ListView):
    model = Textbook
    template_name = 'home.html'

class TextCreateView(CreateView):
    model = Textbook
    template_name = 'text_new.html'
    fields = ['title', 'author', 'new']


    def get_success_url(self):
        return reverse('home')
