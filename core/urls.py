from django.urls import path
from .views import TextListView, TextCreateView

urlpatterns = [
    path('filter/', TextCreateView.as_view(), name='bootstrap_form_new'),
    path('', TextListView.as_view(), name='home'),
]
