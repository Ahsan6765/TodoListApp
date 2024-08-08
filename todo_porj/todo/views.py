from django.shortcuts import render, redirect
from .models import Task


def index(request):
    tasks = Task.objects.all()
    
    if request.method == "POST":
        if 'add-task' in request.POST:
            title = request.POST.get('title')
            Task.objects.create(title=title)
        elif 'complete-task' in request.POST:
            task_id = request.POST.get('task-id')
            task = Task.objects.get(id=task_id)
            task.completed = not task.completed
            task.save()
        elif 'delete-task' in request.POST:
            task_id = request.POST.get('task-id')
            task = Task.objects.get(id=task_id)
            task.delete()

        return redirect('index')

    return render(request, 'todo/index.html', {'tasks': tasks})


