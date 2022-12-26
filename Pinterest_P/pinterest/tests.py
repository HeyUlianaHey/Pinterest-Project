from django.test import TestCase
from django.urls import reverse
from .views import home
from accounts.models import User


class LoginTestCase(TestCase):
    def setUp(self):
        User.objects.create_user(username="John", password="", email='John@22.com')

    def test_url_exists_at_correct_location(self):
        self.client.login(username='John', password="")
        response = self.client.get(reverse('pinterest:home'))
        self.assertEqual(response.status_code, 200)

