from django.shortcuts import render, redirect
from .models import Card, Order
from Publication.models import Posts
from datetime import datetime

# Create your views here.
def create_card(request):
    if request.method == 'POST':
        # Obtener los datos del cuerpo de la solicitud POST
        card_owner = request.user
        card_number = request.POST.get('card_number')
        card_expire = request.POST.get('card_expire')
        card_cvc = request.POST.get('card_cvc')
        card_type = request.POST.get('card_type')

        # Verificar si se proporcionan todos los datos requeridos
        if card_number and card_expire and card_cvc and card_type:
            # Crear una nueva instancia de tarjeta con los datos proporcionados
            new_card = Card.objects.create(
                card_owner=card_owner,
                card_number=card_number,
                card_expire=card_expire,
                card_cvc=card_cvc,
                card_type=card_type
            )
            # Guardar la nueva tarjeta en la base de datos
            new_card.save()
            # Redirigir a alguna página, por ejemplo, a la página de perfil del usuario
            return redirect('core')
        else:
            # Si falta alguno de los datos requeridos, mostrar un mensaje de error o redirigir a alguna otra página
            return render(request, 'create_Card.html', {'message': 'Por favor, completa todos los campos.'})
    else:
        # Si el método de solicitud no es POST, redirigir a alguna otra página o mostrar un mensaje de error
        return render(request, 'create_Card.html')

def create_order(request, post_id):
    if request.method == 'POST':
        # Obtener los datos del cuerpo de la solicitud POST
        payment_method_id = request.POST.get('payment_method')
        rental_period_start = datetime.strptime(request.POST.get('rental_period_start'), '%Y-%m-%d').date()
        rental_period_end = datetime.strptime(request.POST.get('rental_period_end'), '%Y-%m-%d').date()

        # Verificar si se proporcionan todos los datos requeridos
        if payment_method_id and rental_period_start and rental_period_end:
            # Obtener el método de pago y la publicación asociada a la orden
            payment_method = Card.objects.get(pk=payment_method_id)
            publication = Posts.objects.get(pk=post_id)
            # Calcular el total_amount basado en el precio de la publicación y la duración del arriendo
            rental_months = (rental_period_end - rental_period_start).days // 30
            total_amount = publication.price * rental_months
            # Crear una nueva instancia de Order con los datos proporcionados
            new_order = Order.objects.create(
                payment_method=payment_method,
                publication=publication,
                user=request.user,
                rental_period_start=rental_period_start,
                rental_period_end=rental_period_end,
                total_amount=total_amount
            )
            # Guardar la nueva orden en la base de datos
            new_order.save()
            # Redirigir a alguna página, por ejemplo, a la página de perfil del usuario
            return redirect('orders')
        else:
            # Si falta alguno de los datos requeridos, mostrar un mensaje de error o redirigir a alguna otra página
            return render(request, 'create_order.html', {'message': 'Por favor, completa todos los campos.'})
    else:
        # Si el método de solicitud no es POST, redirigir a alguna otra página o mostrar un mensaje de error
        return render(request, 'create_order.html')

def order_list(request):
    # Obtener todas las órdenes creadas
    orders = Order.objects.all()
    # Renderizar el template con la lista de órdenes
    return render(request, 'orders.html', {'orders': orders})