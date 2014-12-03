from django.contrib import admin

from .models import Album

from tracks.models import Track

class TrackInLine(admin.StackedInline):
	model = Track
	extra = 1

class AlbumAdmin(admin.ModelAdmin):
	list_display = ('title', 'artist')
	inlines = [TrackInLine]

admin.site.register(Album, AlbumAdmin)