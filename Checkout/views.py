import paypalrestsdk
from django.shortcuts import render, get_object_or_404, redirect
from django.conf import settings
from django.http import JsonResponse
from Orders.models import Order
from Authentication.models import Data

# Create your views here.
paypalrestsdk.configure({
    "mode": "sandbox",
    "client_id": settings.PAYPAL_CLIENT_ID,
    "client_secret": settings.PAYPAL_CLIENT_SECRET,
})

def paypal_checkout(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    if request.method == 'POST':
        payment = paypalrestsdk.Payment({
            "intent": "sale",
            "payer": {
                "payment_method": "paypal"},
            "redirect_urls": {
                "return_url": request.build_absolute_uri(
                    "/paypal-return?order_id={}".format(order_id)),
                "cancel_url": request.build_absolute_uri(
                    "/paypal-cancel?order_id={}".format(order_id))},
            "transactions": [{
                "amount": {
                    "total": str(order.total_amount + 1),
                    "currency": "USD"
                },
                "description": "This is the payment transaction description."
                }]
            })
        if payment.create():
            order.payment_status = "Approved"
            for link in payment.links:
                if link.method == "REDIRECT":
                    redirect_url = str(link.href)
                    return redirect(redirect_url)
        else:
            return JsonResponse({"error": payment.error})
    else:
        return render(request, 'checkout.html', {'order': order})