from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.edit import CreateView
from .models import Cart

class CartListView(ListView):
    model = Cart
    template_name='cart.html'


class CartCreateView(CreateView):
    model = Cart
    template_name='cart_create.html'
    fields = '__all__'
