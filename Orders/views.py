from django.shortcuts import render, redirect, get_object_or_404
from Renters.models import Acommodation
from Publication.models import Posts
from Payment.models import Card
from .models import Order

# Create your views here.
def create_order(request, acommodation_id, post_id):
    if request.method == "POST":
        acommodation = get_object_or_404(Acommodation, pk=acommodation_id)
        post = get_object_or_404(Posts, pk=post_id)
        shopper = request.user
        seller = post.publisher
        rental_period_start = request.POST.get('start')
        rental_period_end = request.POST.get('end')
        rental_months = (rental_period_end - rental_period_start).days // 30
        total_amount = acommodation.price * rental_months
        payment_method = request.POST.get('method')
        if payment_method == 'Card':
            card_selected = request.POST.get('card')
            card = get_object_or_404(Card, pk=card_selected)
        else:
            card = None
        payment_status = 'Approve'
        order = Order.objects.create(
            acommodation=acommodation,
            shopper=shopper,
            seller=seller,
            rental_period_start=rental_period_start,
            rental_period_end=rental_period_end,
            total_amount=total_amount,
            payment_method=payment_method,
            card_selected=card,
            payment_status=payment_status
        )
        order.save()
        if order in Order.objects.all():
            post.avaliability = False
            post.save()
            acommodation.times_rented += 1
            acommodation.save()
            return redirect('order')
        else:
            return render(request, 'create_order.html', {'message': "Hubo un problema, intentalo de nuevo"})
    return render(request, 'order.html')

def orders_view(request, user_id, filter_by):
    if filter_by == 'shopper':
        user_orders = Order.objects.filter(shopper_id=user_id)
    elif filter_by == 'seller':
        user_orders = Order.objects.filter(seller_id=user_id)
    else:
        user_orders = Order.objects.all()
    return render(request, 'orders.html', {'user_orders': user_orders, 'user_id': user_id, 'filter_type': filter_by})
