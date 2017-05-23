from .models import Task


def all_tasks(request):
    return {
        'all_tasks': Task.objects.all()
    }
