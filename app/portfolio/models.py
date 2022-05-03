from django.db import models
from django.contrib import admin

class Projects(models.Model):
    id = models.AutoField(primary_key=True)
    titre = models.CharField(max_length=100)
    description = models.TextField(max_length=200)
    langage = models.CharField(max_length=100)
    technos = models.CharField(max_length=100)
    annees = models.CharField
    type = models.CharField(max_length=100)
    lien_github = models.TextField(max_length=100, default='github.com')
    

class ProjectsAdmin(admin.ModelAdmin):
    list_display = ('titre' , 'langage' , 'technos', 'lien_github')