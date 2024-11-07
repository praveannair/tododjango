from django.shortcuts import render
from core import models
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import logout

def deleteTodo(request):
    if request.method == "GET":
        todoId = request.GET.get('id')
        models.todo.objects.filter(id=todoId).delete()
    return todo(request)

@login_required
def todo(request):
    if request.method=="POST":
        task = request.POST.get("task")
        c = models.todo(task=task)
        c.save()
    mytodo = models.todo.objects.all()
    data = {'todos':mytodo}
    return render(request,'todo.html',data)

@login_required
def product(request):
    product = models.product.objects.all()
    data = {'products':product}
    return render(request,'product.html',data)


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

def logout_view(request):
    logout(request)
    return todo(request)
