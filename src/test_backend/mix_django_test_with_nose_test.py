import django
from django.test.utils import setup_test_environment, teardown_test_environment

class PycharmDjangoNoseTestCase(django.test.TestCase):
    @classmethod
    def setUpClass(cls):
        setup_test_environment()

    @classmethod
    def tearDownClass(cls):
        teardown_test_environment()
