from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Boards(models.Model):
    name = models.CharField(max_length=30, unique=True)
    description = models.TextField(max_length=300)

    def __str__(self):
        return self.name


class Topics(models.Model):
    subject = models.CharField(max_length=100)
    board_id = models.ForeignKey(Boards, on_delete=models.CASCADE, related_name='topics')
    starter = models.ForeignKey(User, on_delete=models.CASCADE, related_name='topic_starter')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name



class Posts(models.Model):
    message = models.TextField(max_length=4000)
    topic = models.ForeignKey(Topics, on_delete=models.CASCADE, related_name='posts')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    updated_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='+')
