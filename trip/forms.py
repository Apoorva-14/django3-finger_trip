from django.forms import ModelForm
from .models import Trip,Comment



class TripForm(ModelForm):
    class Meta:
        model = Trip
        fields = [
            'title',
            'description',
            'image',
        ]


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = [
            'commenter',
            'trip',
            'comment_text',
        ]
