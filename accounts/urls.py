from django.conf.urls import url
from django.contrib.auth.views import login, logout

from . import views


urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^login/',
        login, {'template_name': 'accounts/login.html'}, name='login'),
    url(r'^logout/$', logout, {'next_page': 'core:index'}, name='logout'),
    url(r'^register/', views.RegisterView.as_view(), name='register'),
    url(r'^tasks/', views.TaskList.as_view(), name='tasks'),
    url(r'^tasks-done/', views.TaskDoneList.as_view(), name='tasks_done'),
    url(r'^update-user/$', views.UpdateUserView.as_view(), name='update_user'),
    url(r'^update-password/$',
        views.UpdatePasswordView.as_view(), name='update_password'),
]
