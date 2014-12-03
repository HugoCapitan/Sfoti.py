from django.contrib import admin

from .models import Track

# Uncoment if actions is done
# from actions import export_as_excel

class TrackAdmin(admin.ModelAdmin):
	list_display = ('title', 'album', 'artist', 'order', 'player', 'es_pharrel')
	list_filter = ('artist', 'album')
	search_fields = ('title', 'artist__first_name')
	list_editable = ('album',)
	# actions = (export_as_excel, )
	raw_id_fields = ('artist', )

	def es_pharrel(self, obj):
		return obj.id == 8

	es_pharrel.boolean = True

admin.site.register(Track, TrackAdmin)
