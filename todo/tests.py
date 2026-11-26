from django.test import TestCase
from django.urls import reverse

from .models import Tag, Task


class TaskListViewTests(TestCase):
    def test_homepage_renders_task_details(self):
        task = Task.objects.create(content="Prepare report")
        task.tags.add(Tag.objects.create(name="Work"))

        response = self.client.get(reverse("index"), HTTP_HOST="localhost")

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Prepare report")
        self.assertContains(response, "Not done")
        self.assertContains(response, "Work")
