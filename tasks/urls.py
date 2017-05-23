from django.conf.urls import url, include

from . import views


urlpatterns = [
    url(r'^$',
        views.TaskList.as_view(),
        name='list'),
    url(r'^create$',
        views.TaskCreate.as_view(),
        name='create'),
    url(r'^(?P<pk>\d+)$',
        views.TaskDetail.as_view(),
        name='detail'),
    url(r'^update/(?P<pk>\d+)$',
        views.TaskUpdate.as_view(),
        name='update'),
    url(r'^delete/(?P<pk>\d+)$',
        views.TaskDelete.as_view(),
        name='delete'),
    url(r'^done/(?P<pk>\d+)$',
        views.TaskDone.as_view(),
        name='done'),
]
