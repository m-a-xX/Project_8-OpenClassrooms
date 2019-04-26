"""File that contains forms tests"""
from django.test import TestCase
from myapp.forms import RegistrationForm


class TestForms(TestCase):
    """Forms tests class"""

    def test_registration_form(self):
        """Registration form validity test"""
        form = RegistrationForm(data={
            'username': 'user',
            'email': 'email@gmail.com',
            'password1': 'iublnredmw',
            'password2': 'iublnredmw',
        })
        self.assertTrue(form.is_valid())

    def test_registration_form_invalid(self):
        """Registration form validity test"""
        form = RegistrationForm(data={})
        self.assertFalse(form.is_valid())