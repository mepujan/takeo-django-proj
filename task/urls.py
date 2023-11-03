from django.urls import path
from .views import get_list_of_task, add_task

app_name = "task"
urlpatterns = [
    path("tasks", get_list_of_task, name="get_list"),
    path("add", add_task, name="add-task")
]
