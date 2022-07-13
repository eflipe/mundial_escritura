from django.urls import path
from .views import add_stories, index, show_stories

app_name = 'eadda_app'

urlpatterns = [
    path('',index, name="index"),
    path('eadda/<slug:song_title_slug>/', show_stories, name="show_stories"),
    path('add',add_stories, name="add_story")

    ]
