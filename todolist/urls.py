from turtle import up
from django.urls import path
from todolist.views import show_todolist
from todolist.views import register
from todolist.views import login_user
from todolist.views import logout_user
from todolist.views import add_task
from todolist.views import todolist_json
from todolist.views import create_task_ajax
from todolist.views import update
from todolist.views import delete_todolist


app_name = 'todolist'

urlpatterns = [
    path('', show_todolist, name='show_todolist'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('add_task/', add_task, name='add_task'),
    path('json/', todolist_json, name='todolist_json'),
    path('create-task-ajax/', create_task_ajax, name="create_task_ajax"),
    path('update/', update, name="update"),
    path('delete/', delete_todolist, name="delete_todolist")
]