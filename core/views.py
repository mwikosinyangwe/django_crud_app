from django.shortcuts import render, redirect, get_object_or_404
from .models import *

from .forms import CreateTodoForm

def home(request):
    if request.method == "POST":
        form = CreateTodoForm(request.POST)
        if form.is_valid():
            form.save()
            form = CreateTodoForm()
    else:
        form = CreateTodoForm()

    todos = Todo.objects.all()
    context = {'form':form, 'todos':todos}
    return render(request, 'home.html', context)


def todo_update(request, pk):
    
    todos = get_object_or_404(Todo, pk=pk)

    if request.method == "POST":
        form = CreateTodoForm(request.POST, instance=todos)
        if form.is_valid():
            form.save()
            return redirect("/")
    else:
        form = CreateTodoForm(instance=todos)

    context = {'todos':todos, 'form': form}
    return render(request, 'todo_update.html', context )

def detail_view(request, pk):
    
    todos = Todo.objects.get(pk = pk)
    context = {'todos':todos}
         
    return render(request, "todo_detail.html", context)

def DeleteTodo(request, pk):

    
    todos = Todo.objects.get(pk=pk)
    if request.method =="POST":

        todos.delete()
        return redirect("/")
        
    
    
        

    return render(request, "todo_delete.html", {'todos':todos})
