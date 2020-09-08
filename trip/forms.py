from django.forms import ModelForm
from .models import Trip, Like

class TripForm(ModelForm):
    class Meta:
        model = Trip
        fields = ['title', 'description', 'image',]
