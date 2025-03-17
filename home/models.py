from django.db import models
from django.utils import timezone

# Create your models here.
class Todo(models.Model):
    title= models.CharField(max_length=500)
    complete= models.BooleanField(default=False)
    created_at = models.DateTimeField(default=timezone.now, editable=False)
    updated_at = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return self.title