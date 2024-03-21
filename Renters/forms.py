from django import forms
from .models import Apartment, Room

class ApartmentForm(forms.ModelForm):
    class Meta:
        model = Apartment
        fields = ['title', 'description', 'price', 'location', 'bedrooms', 'bathrooms', 'image']

class RoomForm(forms.ModelForm):
    class Meta:
        model = Room
        fields = ['title', 'description', 'price', 'location', 'bedrooms', 'bathrooms', 'image']