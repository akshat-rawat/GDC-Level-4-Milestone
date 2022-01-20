from django.shortcuts import render
from django.http import HttpResponseRedirect

tasks = []
completed = []

def task_view(request) :
    return render(request, "tasks.html", {"tasks" : tasks})

def add_task_view(request) :
    task_name = request.GET.get("task")
    tasks.append(task_name)
    return HttpResponseRedirect("/tasks")

def delete_task_view(request, index) :
    del tasks[index-1]
    return HttpResponseRedirect("/tasks")

def complete_task_view(request, index) :
    completed.append(tasks[index-1])
    del tasks[index-1]
    return HttpResponseRedirect("/completed_tasks")

def completed_tasks_view(request) :
    return render(request, "completed.html", {"completed" : completed})