from django import forms
from .models import Stories


class StoryForm(forms.ModelForm):
    views = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    likes = forms.IntegerField(widget=forms.HiddenInput(), initial=0)

    class Meta:
        model = Stories
        fields  = ['author', 'content', 'views', 'likes']
        # widgets = {
        #     'content': forms.Textarea(attrs={'cols': 50, 'rows': 30}),
        # }
