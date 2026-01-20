from django.urls import path
from .views import todo_list, delete_task, clear_tasks, edit_task

urlpatterns = [
    path("", todo_list, name="todo"),
    path("delete/<int:index>/", delete_task, name="delete"),
    path("clear/", clear_tasks, name="clear"),
    path("edit/<int:index>/", edit_task, name="edit"),
]
