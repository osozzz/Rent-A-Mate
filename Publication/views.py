from django.shortcuts import render, redirect, get_object_or_404
from .models import Posts, Reviews
from Authentication.models import Data

# Create your views here.
def create_review_view(request, post_id):
    post = get_object_or_404(Posts, pk=post_id)
    data = get_object_or_404(Data, user=request.user)
    is_saved = post in data.saved_posts.all()

    if request.method == 'POST':
        rating = request.POST.get('rating')
        comments = request.POST.get('comments')
        
        if rating and comments:
            review = Reviews.objects.create(
                publisher=request.user,
                post=post,
                rating=rating,
                comments=comments
            )
            review.save()
            return redirect('publi-and-review', post_id=post_id)
        elif 'save_post' in request.POST:
            # Aquí es donde deberías manejar la lógica de guardar o quitar de favoritos
            if not is_saved:
                data.saved_posts.add(post)
            else:
                data.saved_posts.remove(post)
            return redirect('publi-and-review', post_id=post_id)
        else:
            return render(request, 'posts.html', {'message': 'Por favor, proporciona tanto la calificación como los comentarios.'})
    else:
        return render(request, 'posts.html', {'post': post, 'is_saved': is_saved})

def create_post(request):
    if request.method == 'POST':
        # Obtener los datos del cuerpo de la solicitud POST
        publisher = request.user
        publication_type = request.POST.get('publication_type')
        apartment_id = request.POST.get('apartment_id')
        room_id = request.POST.get('room_id')
        content = request.POST.get('content')
        avaliability = request.POST.get('avaliability')
        price = request.POST.get('price')

        # Verificar si se proporciona tanto el contenido como el tipo de publicación
        if content and publication_type:
            # Crear una nueva instancia de publicación con los datos proporcionados
            new_post = Posts.objects.create(
                publisher=publisher,
                publication_type=publication_type,
                content=content,
                avaliability=avaliability,
                price=price
            )
            # Asignar el apartamento o habitación correspondiente según el tipo de publicación
            if publication_type == 'Apartment' and apartment_id:
                new_post.apartment_id = apartment_id
            elif publication_type == 'Room' and room_id:
                new_post.room_id = room_id
            # Guardar la nueva publicación en la base de datos
            new_post.save()
            # Redirigir a alguna página, por ejemplo, a la página de inicio
            return redirect('core')
        else:
            # Si falta alguno de los datos requeridos, mostrar un mensaje de error o redirigir a alguna otra página
            return render(request, 'create_post.html', {'message': 'Por favor, proporciona tanto el contenido como el tipo de publicación.'})
    else:
        # Si el método de solicitud no es POST, redirigir a alguna otra página o mostrar un mensaje de error
        return render(request, 'create_post.html')