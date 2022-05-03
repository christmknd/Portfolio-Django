from django.shortcuts import render
from portfolio.models import Projects

# Create your views here.

def portfolio(request):
    return render(request,'portfolio.html', {})

def projects(request):
    projects= Projects.objects.all()
    result_project = {'projects' : projects}
    return render(request, 'projects.html',result_project)

def project(request,title):
    project_name = Projects.get(titre=title)
    context = {'project_name': project_name}
    return render(request, 'project.html',context)