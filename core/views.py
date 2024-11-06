from django.shortcuts import render
from core import models
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm


def deleteTodo(request):
    if request.method == "GET":
        todoId = request.GET.get('id')
        models.todo.objects.filter(id=todoId).delete()
    return todo(request)

def todo(request):
    if request.method=="POST":
        task = request.POST.get("task")
        c = models.todo(task=task)
        c.save()
    mytodo = models.todo.objects.all()
    data = {'todos':mytodo}
    return render(request,'todo.html',data)


def signup(request):
     if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/accounts/login')
     else:
        form = UserCreationForm()
     context = {'form': form}
     return render(request, 'signup.html', context)

