from django.shortcuts import render, redirect
from django.urls import reverse
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


def list_songs(request):
    context_dict = {}
    template = 'eadda_app/list_songs.html'
    list_songs = SongInfo.objects.all().order_by('id')
    context_dict['list_songs'] = list_songs

    return render(request, template, context=context_dict)


def add_stories_list(request):
    context_dict = {}
    template = 'eadda_app/add_stories_list.html'
    list_songs = SongInfo.objects.all().order_by('id')
    context_dict['list_songs'] = list_songs

    return render(request, template, context=context_dict)


def add_stories(request, song_title_slug):
    try:
        song = SongInfo.objects.get(slug=song_title_slug)
    except SongInfo.DoesNotExist:
        song = None

    if song is None:
        return redirect('/eadda/')

    form = StoryForm()

    if request.method == 'POST':
        form = StoryForm(request.POST)

        if form.is_valid():
            if song:
                print("Si???")
                story = form.save(commit=False)
                print("Song --->", song)
                print("Form cleaned -->", form.cleaned_data)
                story.id_songs = song
                story.save()

                return redirect(reverse('eadda_app:show_stories', kwargs={'song_title_slug':song.slug}))
        else:
            print(form.errors)

    context_dict = {'form': form, 'song': song}
    template = 'eadda_app/add_story.html'


    return render(request, template, context_dict)
