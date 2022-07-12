from django import forms
from .models import Stories


class StoryForm(forms.ModelForm):
    class Meta:
        model = Stories
        fields  = ['author', 'content']
        widgets = {
            'content': forms.Textarea(attrs={'cols': 50, 'rows': 30}),
        }
