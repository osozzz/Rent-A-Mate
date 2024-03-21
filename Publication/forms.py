from django import forms
from .models import Apartment

class ApartmentForm(forms.ModelForm):
    class Meta:
        model = Apartment
        fields = ['title', 'description', 'price', 'location', 'bedrooms', 'bathrooms', 'image']
