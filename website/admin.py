from django.contrib import admin
from .models import ProjectCategory, Project, BlogModel

# Register your models here.
admin.site.register(ProjectCategory),
admin.site.register(Project),
admin.site.register(BlogModel),
