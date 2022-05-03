from django.urls import path
from portfolio import views

urlpatterns = [
    path('', views.portfolio, name='portfolio'),
    path('projects/<str:title>',views.project, name='project'),
    path('projects',views.projects, name='projects')
]