from django.test import TestCase
from django.urls import reverse

from accounts.models import User


class LoginTestCase(TestCase):
    def setUp(self):
        User.objects.create_user(username="John", password="John2022", email='John@22.com')

    def test_url_exists_at_correct_location(self):
        self.client.login(username='John', password="John2022")
        response = self.client.get(reverse('pinterest:home'))
        self.assertEqual(response.status_code, 200)

    def test_url_exists_at_correct_location_2(self):
        self.client.login(username='John', password="John2022")
        response = self.client.get(reverse('pinterest:search'))
        self.assertEqual(response.status_code, 200)
