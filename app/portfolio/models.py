from django.db import models

class Projects(models.Model):
    titre = models.CharField(max_length=100)
    description = models.TextField(max_length=200)
    langage = models.CharField(max_length=100)
    technos = models.CharField(max_length=100)
    annees = models.CharField
    type = models.CharField(max_length=100)
    lien_github = models.TextField(max_length=100, default='github.com')
