from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views import generic
from django.db.models import Prefetch
from django.views.decorators.http import require_http_methods

from .models import Task, Tag
from .forms import TagForm


@require_http_methods(["POST"])
def toggle_task(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.is_completed = not task.is_completed
    task.save()

    return redirect("todo:index")


class TaskListView(generic.ListView):
    model = Task
    queryset = Task.objects.prefetch_related(Prefetch("tags")).order_by(
        "is_completed", "-created_at"
    )
    template_name = "todo/home.html"
    paginate_by = 10


class TagListView(generic.ListView):
    model = Tag
    template_name = "todo/tags.html"
    paginate_by = 10


class TagCreateView(generic.CreateView):
    model = Tag
    form_class = TagForm
    template_name = "todo/tag-form.html"
    success_url = reverse_lazy("todo:tags")


class TagUpdateView(generic.UpdateView):
    model = Tag
    fields = ["name"]
    template_name = "todo/tag-form.html"
    success_url = reverse_lazy("todo:tags")


class TagDeleteView(generic.DeleteView):
    model = Tag
    template_name = "todo/tag-confirm-delete.html"
    success_url = reverse_lazy("todo:tags")


class TaskCreateView(generic.CreateView):
    model = Task
    fields = ["content", "deadline", "tags", "is_completed"]
    template_name = "todo/task-form.html"
    success_url = reverse_lazy("todo:index")


class TaskUpdateView(generic.UpdateView):
    model = Task
    fields = ["content", "deadline", "tags", "is_completed"]
    template_name = "todo/task-form.html"
    success_url = reverse_lazy("todo:index")


class TaskDeleteView(generic.DeleteView):
    model = Task
    template_name = "todo/task-confirm-delete.html"
    success_url = reverse_lazy("todo:index")
