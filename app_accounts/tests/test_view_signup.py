from django.test import TestCase
from django.urls import reverse, resolve
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from ..views import signupView
from ..forms import SignUpForm


# Create your tests here.
class TestAppAccounts(TestCase):
    def setUp(self):
        self.url = reverse('app_accounts:signup')
        self.view = resolve(self.url)
        self.response = self.client.get(self.url)

    def test_signup_status_code(self):
        self.assertEquals(self.response.status_code, 200)
    
    def test_signup_url_resolve_signup_view(self):
        self.assertEquals(self.view.func, signupView)

    def test_form_contains_csrf_token(self):
        self.assertContains(self.response, 'csrfmiddlewaretoken')

    def test_contains_form(self):
        form = self.response.context.get('form')
        self.assertIsInstance(form, SignUpForm)
    
    def test_form_inputs(self):
        self.assertContains(self.response, '<input', 5)
        self.assertContains(self.response, 'type="text', 1)
        self.assertContains(self.response, 'type="email', 1)
        self.assertContains(self.response, 'type="password', 2)


class SuccesssfulSignupTest(TestCase):
    def setUp(self):
        self.url = reverse('app_accounts:signup')
        data = {
            'username' : 'alaminv2',
            'email' : 'alamin@uslbd.com',
            'password1' : 'a@123456',
            'password2' : 'a@123456'
        }
        self.response = self.client.post(self.url, data)
        self.home_url = reverse('app_boards:home')
    
    def test_redirection(self):
        self.assertRedirects(self.response, self.home_url)
    
    def test_user_creation(self):
        self.assertTrue(User.objects.exists())
    
    def test_user_authentication(self):
        home_response = self.client.get(self.home_url)
        user = home_response.context.get('user')
        self.assertTrue(user.is_authenticated)

class InvalidSignupTest(TestCase):
    def setUp(self):
        self.url = reverse('app_accounts:signup')
        self.response = self.client.post(self.url, {})
    
    def test_redirect_to_same_page(self):
        self.assertEquals(self.response.status_code, 200)
    
    def test_form_error(self):
        form = self.response.context.get('form')
        self.assertTrue(form.errors)
    
    def test_dont_create_user(self):
        self.assertFalse(User.objects.exists())