from django.shortcuts import render
from .models import Stories, SongInfo
from .forms import StoryForm


def index(request):
    # show last story
    stories_list = Stories.objects.order_by('-created_at')[0]
    context_dict = {
        'stories': stories_list
    }
    template = 'eadda_app/index.html'
    return render(request, template, context_dict)


def show_stories(request, song_title_slug):
    context_dict = {}
    template = 'eadda_app/stories.html'

    try:
        song = SongInfo.objects.get(slug=song_title_slug)
        stories = Stories.objects.filter(id_songs=song).order_by('-created_at')

        context_dict['stories'] = stories
        context_dict['song'] = song
    except SongInfo.DoesNotExist:
        context_dict['stories'] = None
        context_dict['song'] = None

    return render(request, template, context=context_dict)


def add_stories(request):
    form = StoryForm
    return render(request, 'eadda_app/stories.html',{ "form" :form})
