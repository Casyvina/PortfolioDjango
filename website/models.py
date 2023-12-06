from django.db import models
from froala_editor.fields import FroalaField
from django.utils import timezone

# Create your models here.
class ProjectCategory(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True)
    
    def __str__(self):
        return self.name

class Project(models.Model):
    category = models.ForeignKey(ProjectCategory, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='portfolio')
    description = models.TextField()
    url = models.URLField(blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-updated', '-created']

    def __str__(self):
        return self.title
 
class BlogModel(models.Model):
    title = models.CharField(max_length=1000)
    content = FroalaField()
    #  slug = models.SlugField(max_length=1000)
    image = models.ImageField(upload_to='blog')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
     
    class Meta:
        ordering = ['-updated', '-created']
     
    def ___str__(self):
         return self.title