from django.urls import path
from .views import get_list_of_task, add_task, delete_task

app_name = "task"
urlpatterns = [
    path("tasks", get_list_of_task, name="get_list"),
    path("add", add_task, name="add-task"),
    path("delete/<int:task_id>", delete_task, name="delete")
]
