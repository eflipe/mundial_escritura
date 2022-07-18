from django.urls import path
from .views import add_stories, index, show_stories, list_songs, add_stories_list

app_name = 'eadda_app'

urlpatterns = [
    path('', index, name="index"),
    path('eadda', index, name="index"),
    path('eadda/lista', list_songs, name="list_songs"),
    path('eadda/add_list', add_stories_list, name="add_stories_list"),
    path('eadda/<slug:song_title_slug>/add/', add_stories, name="add_story"),
    path('eadda/<slug:song_title_slug>/', show_stories, name="show_stories"),

    ]
