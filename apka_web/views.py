from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import render, get_object_or_404, redirect
from .models import Task
from .forms import TaskForm
from django.http import JsonResponse
from django.views.decorators.http import require_POST
# Create your views here.
def todolistResponse(request):
    return HttpResponse("Lista rzeczy do zrobienia")
    title_page = "To Do List"
    options = [
        "option 1",
        "option2",
        "option3"
    ]
    return render(
        request,
        'articles.html',
        {
            'title': title_page,
            'options': options,
            'articles': articles
        }
    )
def task_list(request):
    tasks = Task.objects.all()
    return render(request, 'task_list.html', {'tasks': tasks})

def task_detail(request, pk):
    task = get_object_or_404(Task, pk=pk)
    return render(request, 'task_detail.html', {'task': task})

def task_new(request):
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.save()
            return redirect('task_detail', pk=task.pk)
    else:
        form = TaskForm()
    return render(request, 'task_edit.html', {'form': form})

def task_edit(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == "POST":
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            task = form.save(commit=False)
            task.save()
            return redirect('task_detail', pk=task.pk)
    else:
        form = TaskForm(instance=task)
    return render(request, 'task_edit.html', {'form': form})

def task_delete(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.delete()
    return redirect('task_list')
@require_POST
def toggle_task_completed(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.completed = not task.completed
    task.save()
    return JsonResponse({'completed': task.completed})