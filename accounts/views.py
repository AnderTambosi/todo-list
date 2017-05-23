from django.shortcuts import render
from django.core.urlresolvers import reverse_lazy

from django.views.generic import CreateView, ListView, TemplateView, \
                                 UpdateView, FormView

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.views import login as auth_login

from .forms import UserAdminCreationForm
from .models import User
from tasks.models import Task


class IndexView(LoginRequiredMixin, TemplateView):

    template_name = 'accounts/index.html'


class RegisterView(CreateView):

    model = User
    template_name = 'accounts/register.html'
    form_class = UserAdminCreationForm
    success_url = reverse_lazy('core:index')


class UpdateUserView(LoginRequiredMixin, UpdateView):

    model = User
    template_name = 'accounts/update_user.html'
    fields = ['name', 'email']
    success_url = reverse_lazy('accounts:index')

    def get_object(self):
        return self.request.user


class UpdatePasswordView(LoginRequiredMixin, FormView):

    template_name = 'accounts/update_password.html'
    success_url = reverse_lazy('accounts:index')
    form_class = PasswordChangeForm

    def get_form_kwargs(self):
        kwargs = super(UpdatePasswordView, self).get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

    def form_valid(self, form):
        form.save()
        return super(UpdatePasswordView, self).form_valid(form)


class TaskList(LoginRequiredMixin, ListView):

    context_object_name = 'tasks'
    template_name = 'accounts/tasks.html'
    paginate_by = 5

    def get_queryset(self):
        queryset = Task.objects.filter(user=self.request.user,
                                       done=False).order_by('-pk')
        return queryset


class TaskDoneList(LoginRequiredMixin, ListView):

    context_object_name = 'tasks'
    template_name = 'accounts/tasks_done.html'
    paginate_by = 5

    def get_queryset(self):
        queryset = Task.objects.filter(user=self.request.user,
                                       done=True).order_by('-pk')
        return queryset
