from django.shortcuts import render, redirect
from .models import Task
from .form import TaskForm

# Create your views here.


def get_list_of_task(request):
    tasks = Task.objects.all()
    return render(request, 'task_list.html', {'tasks': tasks})


def add_task(request):
    form = TaskForm()
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/tasks')
    return render(request, 'add_task.html', {'form': form})


def delete_task(request, task_id):
    Task.objects.get(id=task_id).delete()
    return redirect("/tasks")


def mark_as_complete(request, task_id):
    task = Task.objects.get(id=task_id)
    task.is_completed = True
    task.save()
    return render(request, 'task_list.html')
