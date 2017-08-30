from django.test import TestCase


class DummyTestClass(TestCase):
    def setUp(self):
        # Setup run before every test method.
        pass

    def tearDown(self):
        # Clean up run after every test method.
        pass

    def test_something_that_will_always_pass(self):
        self.assertFalse(False)
