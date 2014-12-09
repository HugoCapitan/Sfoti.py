# import json
import time
from .models import Track
from django.contrib.auth.decorators import login_required
from django.core.cache import cache
from django.http import HttpResponse, Http404
from django.shortcuts import render, get_object_or_404
from django.views.decorators.cache import cache_page

@login_required
# @cache_page(60)
def track_view(request, title):
	# Debugear el codigo con ipdb
	# Import ipdb; ipdb.set_trace()

	track = get_object_or_404(Track, title=title)
	bio = track.artist.biography

	# data = cache.get('data_%s' % title)

	# if data is None:
	data = {
		'title': track.title,
		'order': track.order,
		'album': track.album.title,
		'artist': {
		'name': track.artist.first_name,
		'bio': bio
		}
	}
	time.sleep(5)
		# cache.set('data_%s' % title, data)

	# json_data = json.dumps(data)
	# return HttpResponse(json_data, content_type='application/json')

	return render(request, 'track.html', {'track': track, 'bio':bio})


from rest_framework import viewsets
from serializers import TrackSerializer

class TrackViewSet(viewsets.ModelViewSet):
	queryset = Track.objects.all()
	serializer_class = TrackSerializer
	model = Track