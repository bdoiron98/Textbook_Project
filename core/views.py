from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.edit import CreateView
from .models import Textbook


class TextListView(ListView):
    model = Textbook
    template_name = 'bootstrap_form.html'

class TextCreateView(CreateView):
    model = Textbook
    template_name = 'bootstrap_form.html'
    fields = ['title', 'author', 'new']





def BootstrapFilterView(request):
    req
    return render(request, "bootstrap_form.html", {})
