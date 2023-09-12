from django.shortcuts import render, redirect
from .models import Todo
from django.utils import timezone

# Create your views here.
def index(request):
    todolist = Todo.objects.all()
    return render(request, 'index.html',{"list":todolist})

def add(request):
    title = request.POST['title']
    todo = Todo(title=title)
    todo.save()
    return redirect("index")

def update(request,todo_id):
    todo = Todo.objects.get(id=todo_id)
    todo.complete = not todo.complete
    todo.updated_at = timezone.now()
    todo.save()
    return redirect("index")

def delete(request,todo_id):
    todo = Todo.objects.get(id=todo_id)
    todo.delete()
    return redirect("index")