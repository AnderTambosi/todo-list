from django.apps import AppConfig

from watson import search as watson


class TasksConfig(AppConfig):
    name = 'tasks'
    verbose_name = 'Task'
    verbose_name_plural = 'Tasks'

    def ready(self):
        Task = self.get_model('Task')
        watson.register(Task)
