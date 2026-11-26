from django.shortcuts import render
from django.views import generic
from django.db.models import Prefetch

from .models import Task, Tag

# Create your views here.
class TaskListView(generic.ListView):
    model = Task
    queryset = Task.objects.prefetch_related(
        Prefetch("tags")
    )
    template_name = "todo/home.html"
    paginate_by = 10

