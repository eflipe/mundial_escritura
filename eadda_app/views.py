from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from .models import Stories, SongInfo
from .forms import StoryForm, UserForm
from django.contrib.auth.decorators import login_required


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

@login_required
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
                story = form.save(commit=False)
                story.id_songs = song
                story.save()

                return redirect(reverse('eadda_app:show_stories', kwargs={'song_title_slug':song.slug}))
        else:
            print(form.errors)

    context_dict = {'form': form, 'song': song}
    template = 'eadda_app/add_story.html'


    return render(request, template, context_dict)


def register(request):
    registered = False

    if request.method == 'POST':
        user_form = UserForm(request.POST)

        if user_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            registered = True
        else:
            print(user_form.errors)

    else:
        user_form = UserForm()


    template = 'eadda_app/register.html'
    context_dict = {
        'user_form': user_form,
        'registered': registered
        }

    return render(request, template, context_dict)


def user_login(request):
    template = 'eadda_app/login.html'

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                return redirect(reverse('eadda_app:index'))
            else:
                return HttpResponse("Your account is disabled.")
    else:
        return render(request, template)


@login_required
def user_logout(request):
    logout(request)
    return redirect(reverse('eadda_app:index'))
