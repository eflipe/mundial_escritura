from django.urls import path
from .views import add_stories

app_name = 'eadda_app'

urlpatterns = [
    path('add',add_stories, name="add_story")
    ]
