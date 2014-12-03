from django.contrib import admin

from .models import Artist

from albums.models import Album

from tracks.models import Track

class AlbumInLine(admin.StackedInline):
	model = Album
	extra = 1

class TrackInLine(admin.StackedInline):
	model = Track
	extra = 1

class ArtistAdmin(admin.ModelAdmin):
	search_fields = ('first_name', 'last_name')
	filter_horizontal = ('favorite_songs',)
	# filter_vertical = ('favorite_songs',)
	inlines = [AlbumInLine, TrackInLine, ]
	
admin.site.register(Artist, ArtistAdmin)
