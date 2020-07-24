from django import forms
from .models import Feed

class FeedForm(forms.ModelForm):
    class Meta:
        model = Feed
        fields = ['title','url']
        labels = {
            'title': 'Title:',
            'url': 'RSS/Atom URL:'
        }
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'url': forms.URLInput(attrs={'class': 'form-control'})
        }