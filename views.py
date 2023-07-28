from django import forms
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.shortcuts import redirect
from django.shortcuts import render

from .models import Task


# Create your views here.

def index(request):
    if not request.user.is_authenticated:
        return redirect(login)

    id = request.user.id
    name = request.user.first_name
    tasks = Task.objects.filter(user_id=id)
    return render(request, 'main/index.html', {'user_name': name, 'tasks': tasks})


def login(request):
    if request.method == 'POST':
        user = authenticate(request, username=request.POST['email'], password=request.POST['password'])
        # auth_login(request, user, backend='django.contrib.auth.backends.ModelBackend')
        auth_login(request, user)
        return redirect(index)

    return render(request, 'main/authorize.html')


def logout(request):
    auth_logout(request)
    return redirect(login)


def register(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('pass')

        new_user = User.objects.create_user(username=email, email=email, first_name=name, password=password)
        new_user.save()

        user = authenticate(request, username=email, password=password)
        auth_login(request, user)
        return redirect('/')


def addTask(request):
    if request.method == 'POST':
        user_id = request.user.id
        title = request.POST['title']
        new_task = Task(title=title, user_id=user_id)
        new_task.save()

        return redirect('/')


def deleteTask(request, task_id):
    Task.objects.get(id=task_id).delete()
    return redirect('/')
