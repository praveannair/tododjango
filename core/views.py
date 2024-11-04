from django.shortcuts import render
from core import models

def todo(request):
    if request.method=="POST":
        task = request.POST.get("task")
        c = models.todo(task=task)
        c.save()
    mytodo = models.todo.objects.all()
    data = {'todos':mytodo}
    return render(request,'todo.html',data)

# Create your views here.
