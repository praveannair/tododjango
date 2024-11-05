from django.shortcuts import render
from core import models

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

# Create your views here.
