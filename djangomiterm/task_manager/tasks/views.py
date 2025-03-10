from django.shortcuts import render, redirect
from datetime import date, datetime
from .models import Task

# Create your views here.
def task_list (request):
    tasks = Task.objects.all()
    return render(request, 'task_list.html', {'Task': tasks})

def add_task (request):
    return render(request, 'task_form.html')

def save_task (request):
    title = request.POST['title']
    description = request.POST['description']
    due_date_str = request.POST['due_date']
    due_date = datetime.strptime(due_date_str, "%Y-%m-%d").date()
    currentDate = date.today()
    if currentDate <= due_date:
        status = 'Ongoing'
    elif currentDate > due_date:
        status = 'Overdue'
    newTask = Task(title = title, description = description, due_date = due_date, status = status)
    newTask.save()
    return redirect('/')

def edit(request, id):
    tasks = Task.objects.get(id=id)
    return render(request, 'task_edit.html', {'Task': tasks})

def update(request, id):
    tasks = Task.objects.get(id=id)
    tasks.title = request.POST['title']
    tasks.description = request.POST['description']
    due_date_str = request.POST['due_date']
    tasks.due_date = datetime.strptime(due_date_str, "%Y-%m-%d").date()
    currentDate = date.today()
    if currentDate <= tasks.due_date:
        tasks.status = 'Ongoing'
    elif currentDate > tasks.due_date:
        tasks.status = 'Overdue'
    tasks.save()

    return redirect('/')

def confirm_delete(request, id):
    tasks = Task.objects.get(id=id)
    return render(request, 'task_confirm_delete.html', {'Task': tasks})

def deleteTask(request, id):
    tasks = Task.objects.get(id=id)
    tasks.delete()

    return redirect('/')

def task_search(request):
    query = request.GET.get('q')  # Get the search term
    if query:
        results = Task.objects.filter(title__icontains=query)  # Filter tasks by query
    else:
        results = Task.objects.all()  # Show all tasks when query is empty
    
    return render(request, 'task_search.html', {'results': results, 'query': query})