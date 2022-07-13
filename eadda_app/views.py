from django.shortcuts import render
from .models import Stories
from .forms import StoryForm

def index(request):
    context_dict = {
        'boldmessage': 'Prueba 1234'
    }
    template = 'eadda_app/index.html'
    return render(request, template, context_dict)


def add_stories(request):
    form = StoryForm
    return render(request, 'eadda_app/stories.html',{ "form" :form})
