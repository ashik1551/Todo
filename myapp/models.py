from django.db import models
from django.contrib.auth.models import User

class Taskmodel(models.Model):
    task_name=models.CharField(max_length=50,null=False)
    task_description=models.TextField(max_length=200,null=False)
    task_date=models.DateField(auto_now_add=True,)
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    status=models.BooleanField(default=False,)