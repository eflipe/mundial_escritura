from django.shortcuts import render
from .models import Stories
from .forms import StoryForm

def add_stories(request):
    form = StoryForm
    return render(request, 'eadda_app/stories.html',{ "form" :form})
