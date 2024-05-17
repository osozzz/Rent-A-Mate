from dateutil.relativedelta import relativedelta
from django.utils.dateparse import parse_date
from django.shortcuts import render, redirect, get_object_or_404
from Publication.models import Posts
from Payment.models import Card
from Authentication.models import Data
from .models import Order

# Create your views here.
def create_order(request, post_id):
    post = get_object_or_404(Posts, id=post_id)
    shopper_data = get_object_or_404(Data, user=request.user)
    cards = shopper_data.payment_info.all()
    if request.method == "POST":
        shopper = request.user
        seller = post.publisher
        rental_period_start = parse_date(request.POST.get('start'))
        rental_period_end = parse_date(request.POST.get('end'))
        months = relativedelta(rental_period_end - rental_period_start)
        rental_months = months.years *12 + months.months
        total_amount = post.acommodation.price * rental_months
        payment_method = request.POST.get('method')
        if payment_method == 'Card':
            card_selected = request.POST.get('card')
            card = get_object_or_404(Card, pk=card_selected)
        else:
            card = None
        payment_status = 'Approve'
        order = Order.objects.create(
            acommodation=post.acommodation,
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
        order_id = order.id
        if order in Order.objects.all():
            post.avaliability = False
            post.save()
            post.acommodation.times_rented += 1
            post.acommodation.save()
            return redirect('checkout', order_id)
        else:
            return render(request, 'create_order.html', {'message': "Hubo un problema, intentalo de nuevo"})
    return render(request, 'create_order.html', {'post': post, 'cards': cards})

def orders_view(request, filter_by):
    user = request.user
    if filter_by == 'shopper':
        user_orders = Order.objects.filter(shopper_id=user.id)
    elif filter_by == 'seller':
        user_orders = Order.objects.filter(seller_id=user.id)
    else:
        user_orders = Order.objects.all()
    return render(request, 'orders.html', {'user_orders': user_orders, 'filter_type': filter_by})
