from django.test import TestCase

from tasks.models import Task

from model_mommy import mommy


class TestTask(TestCase):

    def setUp(self):
        self.task = mommy.make(Task, title='Task 1')

    def test_task_creation(self):
        self.assertTrue(isinstance(self.task, Task))
        self.assertEqual(self.task.__str__(), self.task.title)
