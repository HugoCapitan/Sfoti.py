from django.contrib import admin

from .models import Track

# Uncoment if actions is done
# from actions import export_as_excel

class TrackAdmin(admin.ModelAdmin):
	list_display = ('id', 'title', 'album', 'artist', 'order', 'player', 'es_taylor')
	list_filter = ('artist', 'album')
	search_fields = ('title', 'artist__first_name')
	list_editable = ('album',)
	# actions = (export_as_excel, )
	raw_id_fields = ('artist', )

	def es_taylor(self, obj):
		return obj.id == 12

	es_taylor.boolean = True

admin.site.register(Track, TrackAdmin)
