# payments/views.py
from django.views.generic.base import TemplateView
from django.shortcuts import render
import stripe

stripe.api_key = 'sk_test_VvR3PZWWQ3HJE9js7iof9fN000fVnveBDv' # use your secret key

class PaymentPageView(TemplateView):
    template_name = 'payment.html'

def charge(request):
    if request.method == 'POST':
        charge = stripe.Charge.create(
            amount=500,  # amount is in cents.
            currency='usd',
            description='A Django charge',
            source=request.POST['stripeToken']
        )
        return render(request, 'charge.html')
