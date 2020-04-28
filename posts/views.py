# I owe you: custom form for books in dropdown
# linda lee @baldwincounty.al.gov
# suzanne.mosley@cardinalhealth.com

from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView
from django.views.generic.edit import CreateView
from django.urls import reverse
from .models import Post, Textbook
# from .models import Textbook
from .forms import CustomPostForm


class PostListView(ListView):
    model = Post
    template_name = 'home.html'

class PostCreateView(CreateView):
    model = Post
    template_name = 'post_new.html'
    form_class = CustomPostForm
    # fields = ['user', 'body', 'title', 'author', 'new']

    def get_success_url(self):
        return reverse('home')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class TextListView(ListView):
    model = Textbook
    template_name = 'home.html'

class TextCreateView(CreateView):
    model = Textbook
    template_name = 'text_new.html'
    fields = ['title', 'author', 'new']


    def get_success_url(self):
        return reverse('home')
