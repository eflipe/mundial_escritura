from django.contrib import admin
from .models import SongInfo, Stories
from .models import UserProfile

admin.site.register(SongInfo)
admin.site.register(Stories)
admin.site.register(UserProfile)
