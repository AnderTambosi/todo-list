from django.test import TestCase
from django.test import Client

from django.conf import settings
from django.core.urlresolvers import reverse

from accounts.models import User
from tasks.models import Task

from model_mommy import mommy


class IndexViewTestCase(TestCase):

    def setUp(self):
        self.url = reverse('accounts:index')
        self.user = mommy.prepare(settings.AUTH_USER_MODEL)
        self.user.set_password('test@123')
        self.user.save()

    def tearDown(self):
        self.user.delete()

    def test_view_ok(self):
        response = self.client.get(self.url)
        self.assertEquals(response.status_code, 302)
        self.client.login(username=self.user.username, password='test@123')


class LoginViewTestCase(TestCase):

    def setUp(self):
        self.client = Client()
        self.url = reverse('accounts:login')
        self.user = mommy.prepare(settings.AUTH_USER_MODEL)
        self.user.set_password('test@123')
        self.user.save()

    def tearDown(self):
        self.user.delete()

    def test_login_ok(self):
        data = {
            'username': self.user.username,
            'password': 'test@123'
        }
        response = self.client.get(self.url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'accounts/login.html')
        response = self.client.post(self.url, data)
        redirect_url = reverse(settings.LOGIN_REDIRECT_URL)
        self.assertRedirects(response, redirect_url)
        self.assertTrue(response.wsgi_request.user.is_authenticated())

    def test_login_error(self):
        data = {
            'username': self.user.username,
            'password': 'test@12345'
        }
        response = self.client.get(self.url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'accounts/login.html')
        response = self.client.post(self.url, data)
        error_msg = ('Please enter a correct username and password.'
                     ' Note that both fields may be case-sensitive.')
        self.assertFormError(response, 'form', None, error_msg)


class RegisterViewTestCase(TestCase):

    def setUp(self):
        self.url = reverse('accounts:register')
        self.client = Client()
        self.response = self.client.get(self.url)

    def test_view_ok(self):
        self.assertEquals(self.response.status_code, 200)
        self.assertTemplateUsed(self.response, 'accounts/register.html')

    def test_register_ok(self):
        data = {
            'username': 'test',
            'password1': 'test@123',
            'password2': 'test@123',
            'email': 'test@test.com'
        }
        response = self.client.post(self.url, data)
        index_url = reverse('core:index')
        self.assertRedirects(response, index_url)
        self.assertEquals(User.objects.count(), 1)

    def test_register_error(self):
        data = {}
        response = self.client.post(self.url, data)
        self.assertFormError(response, 'form', 'username',
                             'This field is required.')
        self.assertFormError(response, 'form', 'password1',
                             'This field is required.')
        self.assertFormError(response, 'form', 'password2',
                             'This field is required.')
        self.assertFormError(response, 'form', 'email',
                             'This field is required.')


class UpdateUserTestCase(TestCase):

    def setUp(self):
        self.client = Client()
        self.url = reverse('accounts:update_user')
        self.user = mommy.prepare(settings.AUTH_USER_MODEL)
        self.user.set_password('test@123')
        self.user.save()

    def tearDown(self):
        self.user.delete()

    def test_upate_ok(self):
        data = {
            'name': 'test',
            'email': 'test@test.com'
        }
        response = self.client.get(self.url)
        self.assertEquals(response.status_code, 302)
        self.client.login(username=self.user.username, password='test@123')
        response = self.client.post(self.url, data)
        accounts_index_url = reverse('accounts:index')
        self.assertRedirects(response, accounts_index_url)
        self.user.refresh_from_db()
        self.assertEquals(self.user.name, 'test')
        self.assertEquals(self.user.email, 'test@test.com')

    def test_update_error(self):
        data = {}
        self.client.login(username=self.user.username, password='test@123')
        response = self.client.post(self.url, data)
        self.assertFormError(response, 'form', 'email',
                             'This field is required.')


class UpdatePasswordTestCase(TestCase):

    def setUp(self):
        self.client = Client()
        self.url = reverse('accounts:update_password')
        self.user = mommy.prepare(settings.AUTH_USER_MODEL)
        self.user.set_password('test@123')
        self.user.save()

    def tearDown(self):
        self.user.delete()

    def test_update_password_ok(self):
        data = {
            'old_password': 'test@123',
            'new_password1': 'test@12345',
            'new_password2': 'test@12345'
        }
        self.client.login(username=self.user.username, password='test@123')
        response = self.client.post(self.url, data)
        self.user.refresh_from_db()
        self.assertTrue(self.user.check_password('test@12345'))

    def test_update_password_error(self):
        data = {}
        self.client.login(username=self.user.username, password='test@123')
        response = self.client.post(self.url, data)
        self.assertFormError(response, 'form', 'old_password',
                             'This field is required.')
        self.assertFormError(response, 'form', 'new_password1',
                             'This field is required.')
        self.assertFormError(response, 'form', 'new_password2',
                             'This field is required.')
        self.assertTrue(self.user.check_password('test@123'))
