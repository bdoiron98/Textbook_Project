from django.urls import path
from .views import CartCreateView, CartListView

# Cart Urls
urlpatterns = [
    path('cart/', CartCreateView.as_view(), name='cart_create'),
    path('', CartListView.as_view(), name='home'),
]
