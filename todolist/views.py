
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.decorators import login_required

from todolist.models import TodoList, Todo
from todolist.forms import TodoForm, TodoListForm


def index(request):
    if request.user.is_authenticated:
        return render(request, 'todolist/index.html', {'form': TodoForm()})
    else:
        return redirect('/auth/login')


def todolist(request, todolist_id):
    todolist = get_object_or_404(TodoList, pk=todolist_id)
    if request.method == 'POST':
        redirect('lists:add_todo', todolist_id=todolist_id)

    return render(
        request, 'todolist/todolist.html',
        {'todolist': todolist, 'form': TodoForm()}
    )


def add_todo(request, todolist_id):
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            user = request.user if request.user.is_authenticated else None
            todo = Todo(
                title=request.POST['description'],
                description=request.POST['description'],
                todolist_id=todolist_id,
                create_user=user
            )
            todo.save()
            return redirect('lists:todolist', todolist_id=todolist_id)
        else:
            return render(request, 'todolist/todolist.html', {'form': form})

    return redirect('lists:index')


@login_required
def overview(request):
    if request.method == 'POST':
        return redirect('lists:add_todolist')
    return render(request, 'todolist/overview.html', {'form': TodoListForm()})


def new_todolist(request):
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            # create default todolist
            user = request.user if request.user.is_authenticated else None
            todolist = TodoList(create_user=user)
            todolist.save()
            todo = Todo(
                description=request.POST['description'],
                todolist_id=todolist.id,
                create_user=user
            )
            todo.save()
            return redirect('lists:todolist', todolist_id=todolist.id)
        else:
            return render(request, 'todolist/index.html', {'form': form})

    return redirect('lists:index')


def add_todolist(request):
    if request.method == 'POST':
        form = TodoListForm(request.POST)
        if form.is_valid():
            user = request.user if request.user.is_authenticated else None
            todolist = TodoList(title=request.POST['title'], create_user=user)
            todolist.save()
            return redirect('lists:todolist', todolist_id=todolist.id)
        else:
            return render(request, 'todolist/overview.html', {'form': form})

    return redirect('lists:index')
