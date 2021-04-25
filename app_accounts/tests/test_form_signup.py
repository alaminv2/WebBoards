from django.test import TestCase
from ..forms import SignUpForm

class SignUpFormTest(TestCase):
    def test_form_has_fields(self):
        form = SignUpForm()
        form_fields = list(form.fields)
        desired_fields = ['username', 'email', 'password1', 'password2']
        self.assertSequenceEqual(form_fields, desired_fields)