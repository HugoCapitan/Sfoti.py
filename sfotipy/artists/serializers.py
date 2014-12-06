from .models import Artist
from rest_framework import serializers


class ArtistSerializer(serializers.HyperlinkedModelSerializer):

	paginate_by = 1

	class Meta:
		model = Artist
		fields = ('id', 'first_name', 'last_name', 'es_taylor')
