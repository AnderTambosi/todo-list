from django.test import TestCase
from django.test import Client

from django.conf import settings
from django.core.urlresolvers import reverse

from tasks.models import Task

from model_mommy import mommy


class TaskListViewTestCase(TestCase):

    def setUp(self):
        self.tasks = mommy.make(Task, _quantity=10)
        self.url = reverse('tasks:list')
        self.client = Client()
        self.user = mommy.prepare(settings.AUTH_USER_MODEL)
        self.user.set_password('test@123')
        self.user.save()

    def tearDown(self):
        self.user.delete()

    def test_view_ok(self):
        response = self.client.get(self.url)
        self.assertEquals(response.status_code, 302)
        self.client.login(username=self.user.username, password='test@123')

    # def test_context(self):
    #     response = self.client.get(self.url)
    #     self.assertEquals(response.status_code, 302)
    #     self.client.login(username=self.user.username, password='test@123')
    #     self.assertTrue('tasks' in response.context)
    #     tasks = response.context['tasks']
    #     self.assertEquals(tasks.count(), 10)


class TaskCreateViewTestCase(TestCase):

    def setUp(self):
        self.client = Client()
        self.url = reverse('tasks:create')
        self.user = mommy.prepare(settings.AUTH_USER_MODEL)
        self.user.set_password('test@123')
        self.user.save()

    def tearDown(self):
        self.user.delete()

    def test_create_ok(self):
        data = {
            'title': 'Task 1',
            'description': 'Task description',
        }
        response = self.client.get(self.url)
        self.assertEquals(response.status_code, 302)
        self.client.login(username=self.user.username, password='test@123')
        response = self.client.post(self.url, data)
        self.assertEquals(Task.objects.count(), 1)

    def test_create_error(self):
        data = {}
        response = self.client.get(self.url)
        self.assertEquals(response.status_code, 302)
        self.client.login(username=self.user.username, password='test@123')
        response = self.client.post(self.url, data)
        self.assertFormError(response, 'form', 'title',
                             'This field is required.')
        self.assertFormError(response, 'form', 'description',
                             'This field is required.')


class TaskDetailViewTestCase(TestCase):

    def setUp(self):
        self.task = mommy.make(Task, title='Task 1',
                               description='Task description')
        self.url = reverse('tasks:detail',
                           kwargs={'pk': self.task.id})
        self.client = Client()
        self.user = mommy.prepare(settings.AUTH_USER_MODEL)
        self.user.set_password('test@123')
        self.user.save()

    def tearDown(self):
        self.user.delete()

    def test_view_ok(self):
        response = self.client.get(self.url)
        self.assertEquals(response.status_code, 302)
        self.client.login(username=self.user.username, password='test@123')

    # def test_context(self):
    #     self.assertTrue('task' in self.response.context)
    #     self.assertEquals(self.response.context['task'].title,
    #                       self.task.title)
    #     self.assertEquals(self.response.context['task'].description,
    #                       self.task.description)


class TaskUpdateViewTestCase(TestCase):

    def setUp(self):
        self.task = mommy.make(Task)
        self.client = Client()
        self.url = reverse('tasks:update',
                           kwargs={'pk': self.task.id})
        self.user = mommy.prepare(settings.AUTH_USER_MODEL)
        self.user.set_password('test@123')
        self.user.save()

    def tearDown(self):
        self.user.delete()

    def test_update_ok(self):
        data = {
            'title': 'Task 1',
            'description': 'Task description',
        }
        response = self.client.get(self.url)
        self.assertEquals(response.status_code, 302)
        self.client.login(username=self.user.username, password='test@123')
        response = self.client.post(self.url, data)
        self.assertEquals(Task.objects.first().title, 'Task 1')
        self.assertEquals(Task.objects.first().description,
                          'Task description')

    def test_update_error(self):
        data = {}
        response = self.client.get(self.url)
        self.assertEquals(response.status_code, 302)
        self.client.login(username=self.user.username, password='test@123')
        response = self.client.post(self.url, data)
        self.assertFormError(response, 'form', 'title',
                             'This field is required.')
        self.assertFormError(response, 'form', 'description',
                             'This field is required.')


class TaskDeleteViewTestCase(TestCase):

    def setUp(self):
        self.task = mommy.make(Task, title='Task 1')
        self.client = Client()
        self.url = reverse('tasks:delete',
                           kwargs={'pk': self.task.id})
        self.user = mommy.prepare(settings.AUTH_USER_MODEL)
        self.user.set_password('test@123')
        self.user.save()

    def test_delete_ok(self):
        response = self.client.get(self.url)
        self.assertEquals(Task.objects.count(), 1)
        self.assertEquals(response.status_code, 302)
        self.client.login(username=self.user.username, password='test@123')
        url_redirect = reverse('tasks:list')
        response = self.client.post(self.url)
        self.assertRedirects(response, url_redirect)
        self.assertEquals(Task.objects.count(), 0)


class TaskDoneViewTestCase(TestCase):

    def setUp(self):
        self.task = mommy.make(Task, title='Task 1')
        self.client = Client()
        self.url = reverse('tasks:done',
                           kwargs={'pk': self.task.id})
        self.user = mommy.prepare(settings.AUTH_USER_MODEL)
        self.user.set_password('test@123')
        self.user.save()

    def tearDown(self):
        self.user.delete()

    def test_update_ok(self):
        self.assertEquals(Task.objects.filter(done=False).count(), 1)
        response = self.client.get(self.url)
        self.assertEquals(response.status_code, 302)
        self.client.login(username=self.user.username, password='test@123')
        response = self.client.get(self.url)
        self.assertEquals(Task.objects.filter(done=False).count(), 0)
        self.assertEquals(Task.objects.filter(done=True).count(), 1)
