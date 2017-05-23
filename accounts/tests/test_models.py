from django.test import TestCase

from accounts.models import User

from model_mommy import mommy


class UserTestCase(TestCase):

    def setUp(self):
        self.user = mommy.make(User, username='admin')

    def test_establishment_creation(self):
        self.assertTrue(isinstance(self.user, User))
        self.assertEquals(self.user.__str__(), self.user.username)
