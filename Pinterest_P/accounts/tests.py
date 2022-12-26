from django.test import TestCase
from django.urls import reverse

from accounts.models import User, Profile


class UserModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        User.objects.create(username='Uliana', email='Ulianaa@18.com')

    def test_username_label(self):
        user = User.objects.get(pk=1)
        field_label = user._meta.get_field('username').verbose_name
        self.assertEquals(field_label, 'username')

    def test_email_label(self):
        user = User.objects.get(pk=1)
        field_label = user._meta.get_field('email').verbose_name
        self.assertEquals(field_label, 'email')

    def test_username_max_length(self):
        user = User.objects.get(pk=1)
        max_length = user._meta.get_field('username').max_length
        self.assertEquals(max_length, 150)

    def test_email_max_length(self):
        user = User.objects.get(pk=1)
        max_length = user._meta.get_field('email').max_length
        self.assertEquals(max_length, 100)

    def test_object_name_is_email(self):
        user = User.objects.get(pk=1)
        expected_object_name = user.email
        self.assertEquals(expected_object_name, str(user))

    def test_url_exists_at_correct_location_user_login(self):
        response = self.client.get(reverse("accounts:user_login"))
        self.assertEqual(response.status_code, 200)

    def test_url_exists_at_correct_location_user_register(self):
        response = self.client.get(reverse("accounts:user_register"))
        self.assertEqual(response.status_code, 200)

    # def test_url_exists_at_correct_location_user_logout(self):
    #     self.client.login(username='John', password="John2022")
    #     response = self.client.get(reverse("accounts:user_logout"))
    #     self.assertEqual(response.status_code, 200)


class UserFixturesModelTest(TestCase):
    fixtures = ['dump.json']

    def test_is_active_label(self):
        user = User.objects.get(username="Lena")
        is_active = user._meta.get_field('is_active').default
        self.assertEquals(is_active, True)

    def test_is_admin_label(self):
        user = User.objects.get(username="Lena")
        is_admin = user._meta.get_field('is_admin').default
        self.assertEquals(is_admin, False)

    def test_username_label(self):
        user = User.objects.get(username="Lena")
        field_label = user._meta.get_field('username').verbose_name
        self.assertEquals(field_label, 'username')

    def test_email_label(self):
        user = User.objects.get(username="Lena", email="Lena@lena.com")
        field_label = user._meta.get_field('email').verbose_name
        self.assertEquals(field_label, 'email')


class ProfileModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        User.objects.create(username='Uliana', email='Ulianaa@18.com')

    def test_first_name_max_length(self):
        user = Profile.objects.get(id=1)
        max_length = user._meta.get_field('fname').max_length
        self.assertEquals(max_length, 300)

    def test_last_name_max_length(self):
        user = Profile.objects.get(id=1)
        max_length = user._meta.get_field('lname').max_length
        self.assertEquals(max_length, 300)

    def test_pronouns_max_length(self):
        user = Profile.objects.get(id=1)
        max_length = user._meta.get_field('pronouns').max_length
        self.assertEquals(max_length, 100)

    def test_website_max_length(self):
        user = Profile.objects.get(id=1)
        max_length = user._meta.get_field('website').max_length
        self.assertEquals(max_length, 100)

    def test_photo_upload_to(self):
        user = Profile.objects.get(id=1)
        field = user._meta.get_field('photo').upload_to
        self.assertEquals(field, 'profiles')

    def test_photo_default(self):
        user = Profile.objects.get(id=1)
        field_2 = user._meta.get_field('photo').default
        self.assertEquals(field_2, 'profiles/default.png')

    def test_object_name_user_username(self):
        user = Profile.objects.get(pk=1)
        expected_object_name = f'{user.user.username} Profile'
        self.assertEquals(expected_object_name, str(user))
