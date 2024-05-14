from django import forms
from .models import Acommodation

class AcommodationForm(forms.ModelForm):
    TYPO_CHOICES = (
        ('Apartment', 'Apartment'),
        ('Room', 'Room'),
        ('Studio', 'Studio'),
        ('House', 'House'),
    )
    typo = forms.ChoiceField(choices=TYPO_CHOICES)
    class Meta:
        model = Acommodation
        fields = ['title',
                'typo', 
                'description', 
                'price', 
                'location', 
                'bedrooms', 
                'bathrooms', 
                'image']
