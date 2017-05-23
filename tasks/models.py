from django.db import models
from django.conf import settings
from django.core.urlresolvers import reverse


class TaskManager(models.Manager):

    def done(self, id):
        return self.filter(id=id).update(done=True)


class Task(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    done = models.BooleanField(default=False)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name='User')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = TaskManager()

    class Meta:
        verbose_name = 'Task'
        verbose_name_plural = 'Tasks'

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('tasks:detail', kwargs={'pk': self.id})
