from django.shortcuts import render, redirect
from .models import Task

# Главная страница — список всех задач
def task_list(request):
    tasks = Task.objects.all().order_by('-created_at')
    return render(request, 'tasks/task_list.html', {'tasks': tasks})

# Добавление задачи
def add_task(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description', '')
        if title:
            Task.objects.create(title=title, description=description)
    return redirect('tasks:task_list')

# Отметка задачи как выполненной
def complete_task(request, task_id):
    task = Task.objects.get(id=task_id)
    task.completed = True
    task.save()
    return redirect('tasks:task_list')

# Удаление задачи
def delete_task(request, task_id):
    task = Task.objects.get(id=task_id)
    task.delete()
    return redirect('tasks:task_list')