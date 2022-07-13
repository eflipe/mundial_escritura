from django.urls import path
from .views import add_stories, index

app_name = 'eadda_app'

urlpatterns = [
    path('',index, name="index"),
    path('add',add_stories, name="add_story")
    ]
