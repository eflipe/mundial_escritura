from django.shortcuts import render
from .models import Stories
from .forms import StoryForm

def index(request):
    # show last story
    stories_list = Stories.objects.order_by('-created_at')[0]
    context_dict = {
        'stories': stories_list
    }
    template = 'eadda_app/index.html'
    return render(request, template, context_dict)


def add_stories(request):
    form = StoryForm
    return render(request, 'eadda_app/stories.html',{ "form" :form})
