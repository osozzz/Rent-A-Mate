from django.urls import path
from Checkout import views as checkoutViews

urlpatterns = [
    path('checkout/<int:order_id>', checkoutViews.paypal_checkout, name="checkout"),
]
