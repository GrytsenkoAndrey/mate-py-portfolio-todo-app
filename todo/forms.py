from django import forms

from .models import Tag, Task


class TagForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = ["name"]
        widgets = {
            "name": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Enter tag name"}
            )
        }

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ["content", "deadline", "tags", "is_completed"]
        labels = {
            "content": "Содержимое",
            "deadline": "Срок выполнения",
            "tags": "Тэги",
            "is_completed": "Выполнено",
        }
        widgets = {
            "content": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Enter task content"}
            ),
            "deadline": forms.DateTimeInput(
                attrs={"class": "form-control", "type": "datetime-local"}
            ),
            "is_completed": forms.CheckboxInput(
                attrs={"class": "form-check-input"}
            ),
            "tags": forms.SelectMultiple(
                attrs={"class": "form-control"}
            ),
        }
