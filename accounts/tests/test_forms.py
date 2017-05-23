from django.test import TestCase

from django.core.urlresolvers import reverse

from accounts.forms import UserAdminCreationForm, UserAdminForm

from model_mommy import mommy


class UserAdminCreationFormTestCase(TestCase):

    def test_valid_data(self):
        data = {
            'username': 'test',
            'email': 'test@test.com',
            'password1': 'test@123',
            'password2': 'test@123'
        }
        form = UserAdminCreationForm(data=data)
        self.assertTrue(form.is_valid())
        user = form.save()
        self.assertEquals(user.username, data['username'])
        self.assertEquals(user.email, data['email'])

    def test_valid_data_error(self):
        data = {}
        form = UserAdminCreationForm(data=data)
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors, {
            'username': ['This field is required.'],
            'email': ['This field is required.'],
            'password1': ['This field is required.'],
            'password2': ['This field is required.']
        })


class UserAdminFormTestCase(TestCase):

    def test_valid_data(self):
        data = {
            'username': 'test',
            'email': 'test@test.com',
            'name': 'Test',
            'is_active': True,
            'is_staff': True
        }
        form = UserAdminForm(data=data)
        self.assertTrue(form.is_valid())
        user = form.save()
        self.assertEquals(user.username, data['username'])
        self.assertEquals(user.email, data['email'])
        self.assertEquals(user.name, data['name'])
        self.assertEquals(user.is_active, data['is_active'])
        self.assertEquals(user.is_staff, data['is_active'])

    def test_valid_data_error(self):
        data = {}
        form = UserAdminForm(data=data)
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors, {
            'username': ['This field is required.'],
            'email': ['This field is required.']
        })
