from django.db import models


# Модель для задач

class Task(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    completed = models.BooleanField(default=False)

    def __str__(self):
        return f"Task: {self.title}"


# Модель для данных спринта
class SprintData(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name='sprint_data')
    assignee = models.CharField(max_length=255)
    status = models.CharField(max_length=50)
    completion_percentage = models.FloatField()

    def __str__(self):
        return f"Sprint for task '{self.task.title}' assigned to {self.assignee}"

