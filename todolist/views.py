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
from django.http import HttpResponse, JsonResponse
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt

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

@login_required(login_url='/todolist/login/')
@csrf_exempt
def update(request, id):
    item = Task.objects.get(pk=id)
    finished = not item.is_finished
    item.is_finished = finished
    item.save()
    return JsonResponse({"is_finished": finished})
    
@login_required(login_url='/todolist/login/')
@csrf_exempt
def delete_todolist(request, id):
    todolist = Task.objects.get(pk=id)
    todolist.delete()
    return redirect('todolist:show_todolist')

def todolist_json(request):
    data = Task.objects.filter(user = request.user)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

@login_required(login_url='/todolist/login/')
@csrf_exempt
def create_task_ajax(request):
    if request.method == "POST":
        user = request.user
        title = request.POST.get("title")
        description = request.POST.get("description")
        create_new_task = Task(user=user, title=title, description=description)
        create_new_task.save()

        return JsonResponse({"pk" : create_new_task.pk, "fields": {
            "date" : create_new_task.date,
            "title" : create_new_task.title,
            "description" : create_new_task.description,
        }})