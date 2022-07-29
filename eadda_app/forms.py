from django import forms
from django.contrib.auth.models import User
from .models import Stories


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(), required=True)
    username = forms.CharField(label='Nombre de usuario', required=True)
    email = forms.CharField(label='Email', required=False)

    class Meta:
        model = User
        fields = ('username', 'email', 'password',)


class StoryForm(forms.ModelForm):
    views = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    likes = forms.IntegerField(widget=forms.HiddenInput(), initial=0)

    class Meta:
        model = Stories
        fields  = ['content', 'views', 'likes']
        widgets = {
            'content': forms.Textarea(attrs={'placeholder':'Escribe aquí!', 'class':"control textarea"}),
        }
