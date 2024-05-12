from django.urls import reverse
from django.test import TestCase

from accounts.models import User
from boards.models import Board


class BoardFixturesModelTest(TestCase):
    fixtures = ['dump.json']

    def test_max_length_title(self):
        user = Board.objects.get(pk=1)
        max_length = user._meta.get_field('title').max_length
        self.assertEquals(max_length, 250)

    def test_max_length_description(self):
        user = Board.objects.get(pk=1)
        max_length = user._meta.get_field('description').max_length
        self.assertEquals(max_length, 250)

    def test_object_name_is_title(self):
        user = Board.objects.get(pk=1)
        expected_object_name = user.title
        self.assertEquals(expected_object_name, str(user))

    def test_is_private_default(self):
        user = Board.objects.get(pk=1)
        field = user._meta.get_field('is_private').default
        self.assertEquals(field, False)

    def test_cover_default(self):
        user = Board.objects.get(pk=1)
        field = user._meta.get_field('cover').default
        self.assertEquals(field, 'boards/default.png')

    def test_blank_description(self):
        user = Board.objects.get(pk=1)
        blank = user._meta.get_field('description').blank
        self.assertEquals(blank, True)

    def test_pins_description(self):
        user = Board.objects.get(pk=1)
        blank = user._meta.get_field('pins').blank
        self.assertEquals(blank, True)


# class WaysTestCase(TestCase):
#
#     def setUp(self):
#         User.objects.create_user(username="John", password="John2022", email='John@22.com')
#
#     def test_url_exists_at_correct_location_create_board(self):
#         self.client.login(username='John', password="John2022")
#         response = self.client.get(reverse('boards:create_board'))
#         self.assertEqual(response.status_code, 200)
