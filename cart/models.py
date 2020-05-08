from django.db import models
from django.conf import settings
from datetime import datetime

class Cart(models.Model):
    user = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True)
    created_at = models.DateTimeField(default=datetime.now)


    TAX_AMOUNT = 19.25

    def price_ttc(self):
        return self.price_ht * (1 + TAX_AMOUNT/100.0)

    def __str__(self):
        return  self.client + " - " + self.product
