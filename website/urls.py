
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('components/', views.components, name='components'),
    path('project/', views.projects, name='project'),
    path('contact/', views.contact, name='contact'),
    path('content/<int:pk>', views.blog_content, name='content'),
]
