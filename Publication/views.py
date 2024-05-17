from django.shortcuts import render, redirect, get_object_or_404
from Authentication.models import Data
from django.http import HttpResponseRedirect, HttpResponseNotFound
from Renters.models import Acommodation
from .models import Posts, Reviews

# Create your views here.
def create_post(request, acommodation_id):
    acommodation = get_object_or_404(Acommodation, id=acommodation_id)
    if request.method == 'POST':
        publisher = request.user
        post = Posts.objects.create(
            publisher=publisher,
            acommodation=acommodation,
        )
        post.save()
        return redirect('publi-and-review', post_id=post.pk)
    return render(request, 'create_post.html')
 
def property_details_view(request, post_id):
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
            if not is_saved:
                data.saved_posts.add(post)
                data.save()
            else:
                data.saved_posts.remove(post)
            return redirect('publi-and-review', post_id=post_id)
        else:
            return render(request, 'property_details.html', {'post': post_id}, {'message': 'Por favor, proporciona tanto la calificación como los comentarios.'})
    return render(request, 'property_details.html', {'post': post}, {'is_saved': is_saved})
