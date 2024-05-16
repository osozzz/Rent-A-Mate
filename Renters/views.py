from django.shortcuts import render, redirect
from .models import Acommodation
from .forms import AcommodationForm

# Create your views here.

def show_acommodations(request):
    accommodations = Acommodation.objects.all()
    return render(request, 'properties.html', {'accommodations': accommodations})

def create_acommodation(request):
    if request.method == 'POST':
        form = AcommodationForm(request.POST, request.FILES)
        if form.is_valid():
            acommodation = form.save(commit=False)
            acommodation.owner = request.user
            acommodation.save()
            return redirect('core')
    else:
        form = AcommodationForm()
    return render(request, 'create_acommodation.html', {'form': form})

def edit_acommodation(request, pk):
    acommodation = Acommodation.objects.get(pk=pk)
    if request.method == 'POST':
        form = AcommodationForm(request.POST, request.FILES, instance=acommodation)
        if form.is_valid():
            form.save()
            return redirect('create_post', pk=acommodation.pk)
    else:
        form = AcommodationForm(instance=acommodation)
    return render(request, 'edit_acommodation.html', {'form': form})

def delete_acommodation(request, pk):
    acommodation = Acommodation.objects.get(pk=pk)
    if request.method == 'POST':
        acommodation.delete()
        return redirect('core')
    return render(request, 'delete_acommodation.html', {'acommodation': acommodation})
