from django.contrib import admin
from .models import Projects , ProjectsAdmin

admin.site.register(Projects,ProjectsAdmin)

