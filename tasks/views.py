import json

from django.shortcuts import get_object_or_404, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.core.urlresolvers import reverse_lazy

from django.views.generic import View, TemplateView, ListView, DetailView, \
                                 RedirectView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Task

from watson import search as watson


class TaskList(LoginRequiredMixin, ListView):

    context_object_name = 'tasks'
    template_name = 'tasks/tasks.html'
    paginate_by = 5

    def get_queryset(self):
        queryset = Task.objects.filter(user=self.request.user,
                                       done=False).order_by('-pk')
        q = self.request.GET.get('q', '')
        if q:
            queryset = watson.filter(queryset, q)
        return queryset


class TaskCreate(LoginRequiredMixin, CreateView):

    model = Task
    fields = ['title', 'description']
    context_object_name = 'task'
    success_url = reverse_lazy('tasks:list')
    template_name = 'tasks/create_task.html'

    def form_valid(self, form):
        object = form.save(commit=False)
        object.user = self.request.user
        object.save()
        return super(TaskCreate, self).form_valid(form)


class TaskUpdate(LoginRequiredMixin, UpdateView):

    model = Task
    context_object_name = 'task'
    success_url = reverse_lazy('tasks:list')
    fields = ['title', 'description']
    template_name = 'tasks/update_task.html'


class TaskDetail(LoginRequiredMixin, DetailView):

    model = Task
    context_object_name = 'task'
    template_name = 'tasks/task.html'


class TaskDelete(LoginRequiredMixin, DeleteView):

    model = Task
    context_object_name = 'task'
    success_url = reverse_lazy('tasks:list')
    template_name = 'tasks/task_confirm_delete.html'


class TaskDone(LoginRequiredMixin, RedirectView):

    def get_redirect_url(self, *args, **kwargs):
        task = get_object_or_404(Task, pk=self.kwargs['pk'])
        task = Task.objects.done(task.id)
        return reverse_lazy('tasks:list')
