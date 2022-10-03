from todolist.models import Task
from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.urls import reverse
from todolist.forms import Input_Form

# Create your views here.
@login_required(login_url='/todolist/login/')
def show_todolist(request):
    task_todolist = Task.objects.filter(user = request.user)
    context = {
        'task_list' : task_todolist
    }
    return render(request, "todolist.html", context)

def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Akun telah berhasil dibuat!')
            return redirect('todolist:login')
    
    context = {'form':form}
    return render(request, 'register.html', context)

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('todolist:show_todolist')
        else:
            messages.info(request, 'Username atau Password salah!')
    context = {}
    return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    return redirect('todolist:login')

def add_task(request):
    if request.method == "POST":
        task_form = Input_Form(request.POST)
        if task_form.is_valid():
            task_form.instance.user = request.user
            task_form.save()
            messages.success(request, 'Task berhasil ditambahkan :)')
            return redirect ('todolist:show_todolist')
    context = {
        'task_list ':'task_todolist',
    }
    return render(request, 'add_task.html', context)