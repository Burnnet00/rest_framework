from django.db import models


class Todo(models.Model):
    title = models.CharField(max_length=150)
    descriptions = models.CharField(max_length=300)
    data = models.DateTimeField(auto_now_add=True)
    done = models.BooleanField(default=False)

    def __str__(self):
        return self.title
