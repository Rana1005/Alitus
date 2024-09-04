
from django.db import models
from authentication.models import UserRegisterModel

# 
class TaskModel(models.Model):
    user = models.ForeignKey(UserRegisterModel, on_delete=models.CASCADE)
    task_name = models.CharField(max_length=100)
    task_description = models.TextField()
    status = models.CharField(max_length=20)
    
