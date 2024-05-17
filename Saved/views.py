from django.shortcuts import render, get_object_or_404
from Authentication.models import Data

# Create your views here.
def saved_list_view(request):
    data = get_object_or_404(Data, user=request.user)
    saved = data.saved_posts.all()
    return render(request, 'saved.html', {'saved': saved})
