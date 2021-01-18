# todo/models.py

from django.db import models
# Create your models here.

# add this
class Todo(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField()
    completed = models.BooleanField(default=False)
    number = models.IntegerField(blank=True,null=True)
    language = models.CharField(max_length=120,blank=True,null=True)
    insult = models.CharField(max_length=120,blank=True,null=True)
    created = models.DateTimeField(blank=True,null=True)
    shown = models.IntegerField(blank=True,null=True)
    createdby = models.CharField(max_length=120,blank=True,null=True)
    active = models.CharField(max_length=120,blank=True,null=True)
    comment = models.TextField(blank=True,null=True)
    
    def _str_(self):
        return self.title