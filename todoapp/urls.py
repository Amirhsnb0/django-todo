from django.urls import path
from .views import  todo_create_item, todo_list_view, todo_remove

app_name = 'todoapp'

urlpatterns = [
    path('',todo_list_view,name='todo_list'),
    path('create/',todo_create_item, name='todo_create'),
    path('<id>remove',todo_remove, name='remove' )
]
