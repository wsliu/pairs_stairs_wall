"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase
from django.test.client import Client
from django_extensions.db.fields.json import loads
from src.pair_stairs.models import Programmer, PairStairs, get_pair_times
from src.test_backend.mix_django_test_with_nose_test import PycharmDjangoNoseTestCase

class TestViews(PycharmDjangoNoseTestCase):

    def test_should_render_add_programmer_page(self):
        response = Client().get('/add_programmer/')
        self.assertEqual(response.status_code, 200)

        self.assertTemplateUsed(response, 'add_programmer.html')

    def test_should_redirect_stairs_after_submission(self):
        response = Client().post('/add_programmer/',{'programmer_name':'susan'}, follow=True)
        self.assertRedirects(response, '/stairs/')
        self.assertTemplateUsed(response, 'stairs.html')

    def test_should_save_programmers(self):
        Client().post('/add_programmer/', {'programmer_name':'susan'})
        self.assertEquals(Programmer.objects.filter(name = "susan").count(), 1, "Programmer 'susan' not found")

    def test_should_add_pair_stairs_in_db_when_save_programmers(self):
        Client().post('/add_programmer/', {'programmer_name':'susan'})
        Client().post('/add_programmer/', {'programmer_name':'aimee'})
        self.assertEquals(PairStairs.objects.filter(first = "susan").filter(second = "aimee").count(), 1)

    def test_should_add_pair_stairs_in_db_when_save_programmers2(self):
        Client().post('/add_programmer/', {'programmer_name':'susan'})
        Client().post('/add_programmer/', {'programmer_name':'aimee'})
        Client().post('/add_programmer/', {'programmer_name':'huanhuan'})
        self.assertEquals(PairStairs.objects.count(), 3)

    def test_should_redirect_to_exception_page_when_add_programmer_which_has_already_exist(self):
        Client().post('/add_programmer/', {'programmer_name':'susan'})
        response = Client().post('/add_programmer/', {'programmer_name':'susan'})
        self.assertTemplateUsed(response, "programmer_exist.html")

    def test_update_times(self):
        Client().post('/add_programmer/', {'programmer_name':'susan'})
        Client().post('/add_programmer/', {'programmer_name':'aimee'})

        old_times = get_pair_times(first = 'susan', second = 'aimee')

        response = Client().get("/update_times/susan_aimee")

        self.assertEqual(old_times + 1, get_pair_times(first='susan', second='aimee'))

        json_data = loads(response.content)
        self.assertEqual(json_data['result'], "success")


