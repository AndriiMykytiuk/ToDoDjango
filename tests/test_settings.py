from unittest import TestCase
from django.conf import settings


class SettingsTest(TestCase):

    def test_server_timezone_unchanged(self):
        target_timezone = 'UTC'
        self.assertEqual(target_timezone, settings.TIME_ZONE)
