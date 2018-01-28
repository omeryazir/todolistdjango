from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.

class TodoList(models.Model):
    title = models.CharField(max_length=128, default='not have todolist title')
    create_date = models.DateTimeField(auto_now=True)
    create_user = models.ForeignKey(User, null=True, related_name='todolists', on_delete=models.CASCADE)

    class Meta:
        ordering = ('create_date',)

    def __str__(self):
        return self.title

    def count(self):
        return self.todos.count()

    def count_finished(self):
        return self.todos.filter(is_finished=True).count()

    def count_open(self):
        return self.todos.filter(is_finished=False).count()


class Todo(models.Model):
    title = models.CharField(max_length=128, default='not have todo title')
    description = models.CharField(max_length=128)
    create_date = models.DateTimeField(auto_now=True)
    deadline = models.DateTimeField(null=True)
    is_finished = models.BooleanField(default=False)
    create_user = models.ForeignKey(User, null=True, related_name='todos', on_delete=models.CASCADE)
    todolist = models.ForeignKey(TodoList, related_name='todos', on_delete=models.CASCADE)

    class Meta:
        ordering = ('create_date',)

    def __str__(self):
        return self.description

    def close(self):
        self.is_finished = True
        self.deadline = timezone.now()
        self.save()

    def reopen(self):
        self.is_finished = False
        self.deadline = None
        self.save()
