from django.shortcuts import render, redirect, get_object_or_404
from Authentication.models import Data
from .models import Card

# Create your views here.
def create_card(request):
    data = get_object_or_404(Data, user=request.user)
    url = 'create_Card.html'
    if request.method == 'POST':
        # Obtener los datos del cuerpo de la solicitud POST
        card_name = request.POST.get('card_name')
        card_number = request.POST.get('card_number')
        card_expire = request.POST.get('card_expire')
        card_cvc = request.POST.get('card_cvc')
        card_type = request.POST.get('card_type')
        # Verificar si se proporcionan todos los datos requeridos
        if card_number and card_expire and card_cvc and card_type and card_name:
            existing_card = data.payment_info.filter(
                card_number=card_number,
                card_expire=card_expire,
                card_cvc=card_cvc,
                card_type=card_type
            ).first()
            if existing_card:
                return render(request, url, {'message': 'Esta tarjeta ya se encuentra guardada en tu cuenta'})
            else:
                # Crear una nueva instancia de tarjeta con los datos proporcionados
                new_card = Card.objects.create(
                    card_name=card_name,
                    card_number=card_number,
                    card_expire=card_expire,
                    card_cvc=card_cvc,
                    card_type=card_type
                )
                # Guardar la nueva tarjeta en la base de datos
                new_card.save()
                data.payment_info.add(new_card)
                return redirect('core')
        else:
            return render(request, url, {'message': 'Por favor, completa todos los campos.'})
    else:
        return render(request, url)

def cards_list(request):
    data = Data.objects.get(user=request.user)
    cards = data.payment_info.all()
    return render(request, 'cards.html', {'cards': cards})
