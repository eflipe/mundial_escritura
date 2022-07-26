from django import forms
from django.contrib.auth.models import User
from .models import Stories


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    username = forms.CharField(label='Nombre de usuario')
    email = forms.CharField(label='Email')

    class Meta:
        model = User
        fields = ('username', 'email', 'password',)


class StoryForm(forms.ModelForm):
    views = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    likes = forms.IntegerField(widget=forms.HiddenInput(), initial=0)

    class Meta:
        model = Stories
        fields  = ['author', 'content', 'views', 'likes']
        # widgets = {
        #     'content': forms.Textarea(attrs={'cols': 50, 'rows': 30}),
        # }
