from django.contrib import admin
from .models import Album
from sorl.thumbnail import get_thumbnail
from tracks.models import Track

class TrackInLine(admin.StackedInline):
	model = Track
	extra = 1

class AlbumAdmin(admin.ModelAdmin):
	list_display = ('title', 'artist', 'imagen_album')
	inlines = [TrackInLine]

	#Thumbnail para que las imagenes no se exedan
	def imagen_album(self, obj):
		return '<img src="%s">' % get_thumbnail(obj.cover, '50x50', format='PNG').url

	imagen_album.allow_tags = True

admin.site.register(Album, AlbumAdmin)