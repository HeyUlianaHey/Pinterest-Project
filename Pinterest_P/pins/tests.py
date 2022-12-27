from django.test import TestCase

from pins.models import Pin, Comment


class PinFixturesModelTest(TestCase):
    fixtures = ['dump.json']

    def test_max_length_title(self):
        user = Pin.objects.get(pk=1)
        max_length = user._meta.get_field('title').max_length
        self.assertEquals(max_length, 250)

    def test_max_length_link(self):
        user = Pin.objects.get(pk=1)
        max_length = user._meta.get_field('link').max_length
        self.assertEquals(max_length, 250)

    def test_object_name_is_title(self):
        user = Pin.objects.get(pk=1)
        expected_object_name = user.title
        self.assertEquals(expected_object_name, str(user))

    def test_is_upload_to_file(self):
        user = Pin.objects.get(pk=1)
        field = user._meta.get_field('file').upload_to
        self.assertEquals(field, 'pins')

    def test_date_created_auto_now_add(self):
        user = Pin.objects.get(pk=1)
        field = user._meta.get_field('date_created').auto_now_add
        self.assertEquals(field, True)


class CommentFixturesModelTest(TestCase):
    fixtures = ['dump.json']

    def test_max_length_text(self):
        user = Comment.objects.get()
        max_length = user._meta.get_field('text').max_length
        self.assertEquals(max_length, 250)

    def test_date_created_auto_now_add(self):
        user = Comment.objects.get()
        field = user._meta.get_field('date_created').auto_now_add
        self.assertEquals(field, True)
