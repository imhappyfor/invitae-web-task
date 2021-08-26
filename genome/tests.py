from django.urls import resolve, reverse
from django.test import TestCase

from .views import upload


class UploadTest(TestCase):

    def test_upload_url_resolves_to_upload_view(self):
        found = resolve(reverse('genome:upload'))
        self.assertEqual(found.func, upload)
