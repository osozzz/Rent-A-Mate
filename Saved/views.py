from django.shortcuts import render

# Create your views here.
def saved_list_view(request):
    return render(request, 'saved.html')
