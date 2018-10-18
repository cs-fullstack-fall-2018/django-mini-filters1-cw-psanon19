from django.db import models


# Simple model to hold a todo reminder
class ToDo(models.Model):
    name = models.CharField(max_length=50)
    due_date = models.DateField()

    def __str__(self):
        return self.name
