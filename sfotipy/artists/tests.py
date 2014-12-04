from django.test import TestCase

from .models import Artist
from tracks.models import Track
from albums.models import Album

class TestArtist(TestCase):

	def setUp(self):
		self.artist = Artist.objects.create(first_name='AC/DC')
		self.album = Album.objects.create(title='Razors age', artist=self.artist)
		self.track = Track.objects.create(title='Thunderstruck', artist=self.artist, album=self.album, order=01)

	def test_existe_vista(self):
		res = self.client.get('/artists/%d/' % self.artist.id)
		self.assertEqual(res.status_code, 200)
		self.assertTrue('AC/DC' in res.content)

	def test_usuario_logeado(self):
		res = self.client.get('/tracks/%s/' % self.track.title)
		self.assertEqual(res.status_code, 302)

	def test_no_existe_vista(self):
		id_viejo = self.artist.id
		self.artist.delete()
		res = self.client.get('/artists/%d/' % id_viejo)
		self.assertEqual(res.status_code, 404)