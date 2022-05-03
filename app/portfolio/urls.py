from django.urls import path
from portfolio import views

urlpatterns = [
    path('', views.projects, name='projects'),
    path('projects/<int:id>',views.project, name='project'),
]